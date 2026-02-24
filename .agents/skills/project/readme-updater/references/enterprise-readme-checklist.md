# Enterprise README Checklist

## Purpose
Use this checklist to evaluate whether a README is enterprise-ready and actionable for engineering, operations, and governance stakeholders.

## Acceptance Criteria
- README explains what the system does, for whom, and what is out of scope.
- Setup steps are reproducible from a clean machine.
- Environment variable documentation is complete for local and CI usage.
- Build/test/lint commands are accurate and current.
- Deployment notes state how releases are produced and promoted.
- Security section covers secrets handling and reporting channel.
- Ownership/support section names responsible team or escalation path.
- Contribution section explains branching, PR, and quality expectations.

## Section-Level Prompts

### Overview
- Can a new engineer understand domain purpose in under 2 minutes?
- Is business value stated without marketing language?

### Setup
- Are prerequisites explicit (versioned tools)?
- Is there a fast path and a full path?

### Configuration
- Are all required variables documented with meaning and examples?
- Are secrets clearly separated from non-sensitive config?

### Operations
- Are run and debug instructions present?
- Are common failure modes and first-response actions documented?

### Governance
- Are ownership, contribution workflow, and release responsibilities clear?

## Severity Model
- Critical: Blocks onboarding or safe operation.
- Major: Causes confusion or high support burden.
- Minor: Stylistic or discoverability improvements.

## Suggested Review Output
- Findings grouped by severity.
- Exact README section or line reference.
- Concrete fix recommendation.
- Residual unknowns labeled `TBD (owner needed)`.