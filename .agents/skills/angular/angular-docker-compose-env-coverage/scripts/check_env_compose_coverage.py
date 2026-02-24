#!/usr/bin/env python3
"""Check that .env variables are covered by docker-compose configuration."""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
from dataclasses import dataclass

COMPOSE_CANDIDATES = (
    "docker-compose.yml",
    "docker-compose.yaml",
    "compose.yml",
    "compose.yaml",
)

ENV_DEFAULT_GLOBS = (".env", ".env.*")
ENV_DEFAULT_EXCLUDES = {".env.example", ".env.sample", ".env.template"}


@dataclass
class CoverageResult:
    env_file: pathlib.Path
    missing: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate that .env variables are covered by docker-compose."
    )
    parser.add_argument("--project-root", default=".", help="Project root path.")
    parser.add_argument(
        "--compose-file",
        default=None,
        help="Compose file path. Auto-detected when omitted.",
    )
    parser.add_argument(
        "--mode",
        choices=("referenced", "strict"),
        default="referenced",
        help="Coverage mode. 'strict' requires explicit env/arg wiring.",
    )
    parser.add_argument(
        "--env-glob",
        action="append",
        default=[],
        help="Glob for env files (repeatable). Defaults: .env and .env.*",
    )
    parser.add_argument(
        "--exclude-env",
        action="append",
        default=[],
        help="Env file basename to exclude (repeatable).",
    )
    return parser.parse_args()


def find_compose_file(project_root: pathlib.Path, compose_file: str | None) -> pathlib.Path:
    if compose_file:
        path = (project_root / compose_file).resolve()
        if not path.exists():
            raise FileNotFoundError(f"Compose file not found: {path}")
        return path

    for name in COMPOSE_CANDIDATES:
        candidate = project_root / name
        if candidate.exists():
            return candidate.resolve()

    raise FileNotFoundError(
        "Compose file not found. Expected one of: " + ", ".join(COMPOSE_CANDIDATES)
    )


def collect_env_files(project_root: pathlib.Path, globs: list[str], excludes: set[str]) -> list[pathlib.Path]:
    patterns = tuple(globs) if globs else ENV_DEFAULT_GLOBS
    files: list[pathlib.Path] = []
    seen: set[pathlib.Path] = set()

    for pattern in patterns:
        for path in project_root.glob(pattern):
            resolved = path.resolve()
            if not resolved.is_file():
                continue
            if resolved.name in excludes:
                continue
            if resolved in seen:
                continue
            files.append(resolved)
            seen.add(resolved)

    return sorted(files)


def load_env_keys(env_file: pathlib.Path) -> list[str]:
    keys: list[str] = []
    key_pattern = re.compile(r"^(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=")

    for line in env_file.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        match = key_pattern.match(stripped)
        if match:
            keys.append(match.group(1))

    return sorted(set(keys))


def has_env_file_reference(compose_text: str, env_file: pathlib.Path, project_root: pathlib.Path) -> bool:
    candidates = {env_file.name}
    try:
        rel = env_file.relative_to(project_root)
        candidates.add(str(rel).replace("\\", "/"))
    except ValueError:
        pass

    for candidate in candidates:
        escaped = re.escape(candidate)
        # Match common env_file entries like: env_file: .env or - ./.env.local
        if re.search(rf"(?m)^\s*-?\s*['\"]?\.{{0,2}}/?{escaped}['\"]?\s*$", compose_text):
            return True
        if re.search(rf"(?m)^\s*env_file\s*:\s*['\"]?\.{{0,2}}/?{escaped}['\"]?\s*$", compose_text):
            return True
    return False


def is_key_covered(compose_text: str, key: str, mode: str) -> bool:
    escaped = re.escape(key)

    # Generic compose interpolation patterns.
    ref_pattern = rf"\$\{{{escaped}(?::[-+?][^}}]*)?\}}"
    direct_ref_pattern = rf"\${escaped}(?![A-Za-z0-9_])"

    # Common explicit mappings in environment lists/maps and build args.
    explicit_patterns = (
        rf"(?m)^\s*-\s*{escaped}\s*=\s*.*$",
        rf"(?m)^\s*-\s*{escaped}\s*$",
        rf"(?m)^\s*{escaped}\s*:\s*.*$",
    )

    if mode == "strict":
        return any(re.search(pattern, compose_text) for pattern in explicit_patterns)

    if re.search(ref_pattern, compose_text) or re.search(direct_ref_pattern, compose_text):
        return True

    return any(re.search(pattern, compose_text) for pattern in explicit_patterns)


def check_coverage(
    compose_file: pathlib.Path,
    env_files: list[pathlib.Path],
    mode: str,
    project_root: pathlib.Path,
) -> list[CoverageResult]:
    compose_text = compose_file.read_text(encoding="utf-8")
    results: list[CoverageResult] = []

    for env_file in env_files:
        keys = load_env_keys(env_file)
        missing: list[str] = []

        env_file_reference = has_env_file_reference(compose_text, env_file, project_root)
        for key in keys:
            if env_file_reference and mode == "referenced":
                continue
            if not is_key_covered(compose_text, key, mode):
                missing.append(key)

        results.append(CoverageResult(env_file=env_file, missing=missing))

    return results


def main() -> int:
    args = parse_args()
    project_root = pathlib.Path(args.project_root).resolve()

    excludes = set(ENV_DEFAULT_EXCLUDES)
    excludes.update(args.exclude_env)

    try:
        compose_file = find_compose_file(project_root, args.compose_file)
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    env_files = collect_env_files(project_root, args.env_glob, excludes)
    if not env_files:
        print("No env files found. Nothing to check.")
        return 0

    results = check_coverage(compose_file, env_files, args.mode, project_root)

    missing_total = 0
    for result in results:
        if not result.missing:
            print(f"PASS {result.env_file.name}: all variables are covered")
            continue

        missing_total += len(result.missing)
        missing_display = ", ".join(result.missing)
        print(f"FAIL {result.env_file.name}: missing {len(result.missing)} variable(s): {missing_display}")

    if missing_total:
        print(
            f"\nCoverage check failed ({missing_total} missing variables). "
            "Update docker-compose mappings and re-run.",
            file=sys.stderr,
        )
        return 1

    print("\nCoverage check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
