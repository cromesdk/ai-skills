#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

const SKIP_DIRS = new Set(['node_modules', 'dist', '.git']);
const EXTENSIONS = /\.(ts|tsx|mts|cts)$/;
const IMPORT_PATTERNS = [
  // import ... from './x', export ... from './x', import './x', export * from './x'
  /\b(?:import|export)\s+(?:(?:type\s+)?(?:[\w*\s{},]+)\s+from\s+)?(['"])(\.\/[^'"]+|\.\.\/[^'"]+)\1/g,
  // dynamic import('./x')
  /\bimport\s*\(\s*(['"])(\.\/[^'"]+|\.\.\/[^'"]+)\1\s*\)/g,
];

function parseArgs() {
  const args = process.argv.slice(2);
  let fix = false;
  const dirs = [];
  for (const arg of args) {
    if (arg === '--fix') fix = true;
    else if (arg.startsWith('--dir=')) dirs.push(arg.slice(6));
  }
  return { fix, dirs: dirs.length ? dirs : ['src'] };
}

function* walkDir(root, base = '') {
  const full = path.join(root, base);
  let entries;
  try {
    entries = fs.readdirSync(full, { withFileTypes: true });
  } catch (_err) {
    return;
  }
  for (const ent of entries) {
    const rel = base ? path.join(base, ent.name) : ent.name;
    if (ent.isDirectory()) {
      if (SKIP_DIRS.has(ent.name)) continue;
      yield* walkDir(root, rel);
    } else if (EXTENSIONS.test(ent.name)) {
      yield path.join(root, rel);
    }
  }
}

function normalizeSpecifier(spec) {
  if (
    spec.endsWith('.js') ||
    spec.endsWith('.mjs') ||
    spec.endsWith('.cjs') ||
    spec.endsWith('.json') ||
    spec.endsWith('.node')
  ) {
    return null;
  }

  if (spec.includes('?') || spec.includes('#')) return null;

  if (spec.endsWith('.ts')) return spec.slice(0, -3) + '.js';
  if (spec.endsWith('.tsx')) return spec.slice(0, -4) + '.js';
  if (spec.endsWith('.mts')) return spec.slice(0, -4) + '.mjs';
  if (spec.endsWith('.cts')) return spec.slice(0, -4) + '.cjs';

  return spec + '.js';
}

function findRelativeImports(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const lines = content.split(/\r?\n/);
  const issues = [];

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const seenSpecs = new Set();

    for (const pattern of IMPORT_PATTERNS) {
      pattern.lastIndex = 0;
      let match;
      while ((match = pattern.exec(line)) !== null) {
        const quote = match[1];
        const spec = match[2];

        if (seenSpecs.has(spec)) continue;

        const fixed = normalizeSpecifier(spec);
        if (!fixed || fixed === spec) continue;

        seenSpecs.add(spec);
        issues.push({
          lineIndex: i,
          line,
          spec,
          fixed,
          quote,
        });
      }
    }
  }
  return issues;
}

function fixFile(filePath, issues) {
  const content = fs.readFileSync(filePath, 'utf8');
  const lines = content.split(/\r?\n/);
  const byLine = new Map();
  for (const issue of issues) {
    const list = byLine.get(issue.lineIndex) || [];
    list.push(issue);
    byLine.set(issue.lineIndex, list);
  }
  for (const [lineIndex, lineIssues] of byLine) {
    let line = lines[lineIndex];
    for (const { spec, fixed, quote } of lineIssues) {
      const escapedSpec = spec.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      const escapedQuote = quote === "'" ? "'" : '\\"';
      const re = new RegExp(`${escapedQuote}${escapedSpec}${escapedQuote}`, 'g');
      line = line.replace(re, `${quote}${fixed}${quote}`);
    }
    lines[lineIndex] = line;
  }
  fs.writeFileSync(filePath, lines.join('\n'), 'utf8');
}

function main() {
  const { fix, dirs } = parseArgs();
  const cwd = process.cwd();
  const allIssues = [];

  for (const dir of dirs) {
    const root = path.resolve(cwd, dir);
    if (!fs.existsSync(root) || !fs.statSync(root).isDirectory()) {
      console.warn('Skip (missing or not a directory):', root);
      continue;
    }
    for (const filePath of walkDir(root)) {
      const issues = findRelativeImports(filePath);
      if (issues.length) {
        allIssues.push({ filePath, issues });
      }
    }
  }

  for (const { filePath, issues } of allIssues) {
    const relPath = path.relative(cwd, filePath);
    for (const { lineIndex, spec, fixed } of issues) {
      console.log(`${relPath}:${lineIndex + 1}: ${spec} -> ${fixed}`);
    }
    if (fix && issues.length) {
      fixFile(filePath, issues);
    }
  }

  if (allIssues.length === 0) {
    console.log('No relative imports missing emitted extensions found.');
    process.exit(0);
    return;
  }

  const total = allIssues.reduce((n, { issues }) => n + issues.length, 0);
  if (fix) {
    console.log(`Fixed ${total} import(s) in ${allIssues.length} file(s).`);
  } else {
    console.log(
      `Found ${total} import(s) missing emitted extensions in ${allIssues.length} file(s). Run with --fix to update.`
    );
    process.exit(1);
  }
}

main();