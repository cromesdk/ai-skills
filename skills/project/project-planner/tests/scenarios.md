# Skill Evaluation Scenarios

## Scenario 1: Complete planning input with fixed deadline and team (easy)
### Input
User asks: "Plan delivery of a customer portal MVP in 8 weeks with a 4-person team. Scope includes auth, dashboard, billing, and admin reporting."

### Repository/Context State
- Deadline is explicit.
- Team capacity is explicit.
- Scope is explicit.

### Expected behavior
- Produces full output contract sections in required order.
- Defines milestone sequence with validation gates.
- Provides WBS with actionable tasks and done criteria.
- Includes dependency mapping and explicit critical path statement.
- Provides effort/timeline estimates with confidence markers.
- Includes immediate next actions (3 to 5 items).

## Scenario 2: Multi-stream program with shared dependencies and conflicts (hard)
### Input
User asks: "Create a plan for API modernization and frontend migration running in parallel. Backend team is blocked by security review windows; frontend depends on API contracts."

### Repository/Context State
- Multiple streams with shared dependency points.
- Conflicting constraints between velocity and governance windows.

### Expected behavior
- Separates workstreams while preserving cross-stream dependencies.
- Identifies bottlenecks and shared blockers.
- Highlights critical path across both streams.
- Proposes deterministic sequencing that minimizes idle time.
- Keeps output schema order intact despite multi-stream complexity.

## Scenario 3: Sparse request with missing critical inputs (edge)
### Input
User asks: "Make me a project plan for our rewrite."

### Repository/Context State
- No explicit timeline.
- No staffing or capacity data.
- No definition of done.

### Expected behavior
- Asks focused clarifying questions for mission-critical inputs.
- If unanswered, proceeds with explicit assumptions.
- Marks assumptions and open questions in dedicated section.
- Uses low-confidence estimates where uncertainty remains.
- Avoids fabricated constraints or staffing details.

## Scenario 4: Unrealistic deadline requiring tradeoff proposal (edge)
### Input
User asks: "Deliver full platform migration in 2 weeks with current 2-person team and no overtime."

### Repository/Context State
- Deadline appears infeasible for requested scope/capacity.

### Expected behavior
- Explicitly calls out infeasibility.
- Proposes concrete tradeoffs: scope reduction, capacity increase, or timeline shift.
- Preserves deterministic task and milestone structure for chosen option.
- Does not silently accept impossible constraints.
- States confidence impact and required schedule buffer for each tradeoff path.

## Scenario 5: Missing owners and uncertain resourcing (edge)
### Input
User asks: "Build a rollout plan for SSO and audit logging."

### Repository/Context State
- Owners are unknown.
- Capacity allocation is unknown.

### Expected behavior
- Uses owner roles where named owners are unavailable.
- Tracks owner/resource gaps under assumptions/open questions.
- Includes explicit risk entries for staffing uncertainty.
- Keeps next actions actionable despite ownership gaps.
- Includes at least one open question that unblocks owner assignment.

## Scenario 6: Replanning after mid-project scope change (hard)
### Input
User asks: "Replan the release. We added enterprise SAML and audit export after sprint 2."

### Repository/Context State
- Existing plan already in progress.
- New scope changes dependencies and likely timeline.

### Expected behavior
- Produces revised plan with updated milestones and dependencies.
- Highlights delta impacts on critical path, estimates, and risks.
- Preserves completed/in-flight work where possible.
- Lists immediate next actions for transition from old plan to revised plan.
- Clearly distinguishes unchanged tasks from modified or newly added tasks.
