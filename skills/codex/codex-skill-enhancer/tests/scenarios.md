# Test Scenarios for codex-skill-enhancer

## Scenario: Improve trigger quality and portability

**Difficulty:** Easy

**Query:** Improve this skill so it triggers reliably for refactor and review requests across Codex, Cursor, and Copilot workflows.

**Expected behaviors:**

1. Reads current skill files
   - **Minimum:** Reads `SKILL.md`
   - **Quality criteria:**
     - Reads `SKILL.md` and checks `tests/scenarios.md` if present
     - Reads `agents/openai.yaml` or creates it when missing
     - Summarizes current trigger phrases
     - Identifies assistant-specific wording that reduces portability
   - **Weight:** 3

2. Runs proactive assessment without unnecessary questioning
   - **Minimum:** Identifies improvement targets autonomously
   - **Quality criteria:**
     - Does not ask generic "what should improve?" questions
     - Proposes high-impact improvements directly
     - Asks questions only if blocked by missing critical context
   - **Weight:** 5

3. Produces structured enhancement plan
   - **Minimum:** Proposes changes
   - **Quality criteria:**
     - Separates user-requested, technical, and portability fixes
     - Includes `agents/openai.yaml` alignment as an explicit task
     - Prioritizes user-requested fixes first
   - **Weight:** 4

4. Creates and uses a TODO checklist
   - **Minimum:** Creates a TODO list before implementation
   - **Quality criteria:**
     - Uses clear status markers (`[ ]`, `[-]`, `[x]`)
     - Keeps exactly one in-progress item at a time
     - Updates status as tasks complete
     - Includes verification tasks in TODO tracking
   - **Weight:** 5

5. Provides official references
   - **Minimum:** Includes a references section in final output
   - **Quality criteria:**
     - Uses official docs links only when available
     - References are relevant to specific changes made
     - Includes title + URL for each source
   - **Weight:** 5

**Output validation:**
- If agent asks generic "what should I improve?" before analyzing files, score = 0 for behavior 2
- If final output has no references section, score = 0 for behavior 5

---

## Scenario: Update this skill in place

**Difficulty:** Easy

**Query:** $codex-skill-enhancer update Skill codex-skill-enhancer

**Expected behaviors:**

1. Resolves in-place target correctly
   - **Minimum:** Uses the currently invoked skill directory as target
   - **Quality criteria:**
     - Does not ask for a path when current skill path is explicit
     - States one-line reason for using this skill
     - Begins baseline assessment immediately
   - **Weight:** 5

2. Applies deterministic, minimal edits
   - **Minimum:** Updates `SKILL.md`
   - **Quality criteria:**
     - Keeps edits scoped to identified issues only
     - Avoids unnecessary folder or file renames
     - Maintains existing intent while improving clarity and actionability
   - **Weight:** 5

3. Aligns companion files
   - **Minimum:** Updates `agents/openai.yaml` if wording is out of sync
   - **Quality criteria:**
     - `short_description` matches skill purpose
     - `default_prompt` reflects current workflow and outputs
     - Adds or updates test coverage for the in-place update request shape
   - **Weight:** 4

4. Reports evidence and completion
   - **Minimum:** Includes changed files and reason
   - **Quality criteria:**
     - Includes final TODO snapshot
     - Includes references section with official docs
     - Mentions any remaining risk explicitly
   - **Weight:** 4

---

## Scenario: Prevent assistant-specific lock-in

**Difficulty:** Medium

**Query:** Rewrite this skill because it is too Codex-specific and fails in other coding assistants.

**Expected behaviors:**

1. Detects lock-in language
   - **Minimum:** Finds at least one assistant-specific phrase
   - **Quality criteria:**
     - Replaces platform-specific wording with generic agent phrasing
     - Keeps optional compatibility notes concise
   - **Weight:** 4

2. Preserves useful intent while generalizing
   - **Minimum:** Maintains workflow function
   - **Quality criteria:**
     - Does not remove core behavior
     - Keeps instructions imperative and testable
   - **Weight:** 4

3. Updates tests to cover portability regressions
   - **Minimum:** Adds or edits one relevant scenario
   - **Quality criteria:**
     - Includes expected behavior for cross-assistant consistency
     - Verifies `agents/openai.yaml` wording remains assistant-agnostic
   - **Weight:** 3

4. Maintains TODO hygiene during refactor
   - **Minimum:** Updates TODO statuses during work
   - **Quality criteria:**
     - Does not mark tasks complete before changes are applied
     - Leaves a final TODO snapshot with all done items clearly marked
   - **Weight:** 3

5. Grounds portability claims in official docs
   - **Minimum:** Cites at least one official source per assistant ecosystem discussed
   - **Quality criteria:**
     - Uses official docs for Codex/OpenAI, Cursor, and GitHub Copilot when claims are made
     - Avoids forum or blog links as primary evidence
   - **Weight:** 4

---

## Scenario: Handle missing path safely

**Difficulty:** Edge-case

**Query:** Enhance skill at ./skills/does-not-exist/

**Expected behaviors:**

1. Reports missing target clearly
   - **Minimum:** States path not found
   - **Quality criteria:**
     - Does not fabricate analysis
     - Explains the blocker in one clear sentence
   - **Weight:** 4

2. Offers recovery actions
   - **Minimum:** Asks for corrected path
   - **Quality criteria:**
     - Offers to search nearby directories
     - Waits for confirmation before editing
   - **Weight:** 4

3. Handles TODO list correctly when blocked
   - **Minimum:** Does not fabricate completion
   - **Quality criteria:**
     - If TODO exists, marks blocked items as pending
     - Does not mark blocked tasks as complete
   - **Weight:** 4

4. Handles references correctly when blocked
   - **Minimum:** Does not fabricate references
   - **Quality criteria:**
     - States that references were not gathered due to blocker when no external changes were applied
     - Avoids adding unrelated links just to satisfy format
   - **Weight:** 3
