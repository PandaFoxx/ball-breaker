---
name: reviewer
description: Reviews completed implementation tasks against acceptance criteria and quality standards, passing or sending back for rework.
---

# reviewer

The reviewer skill is the quality gate of the workflow. It picks a completed task from `02_review`, evaluates it against the defined acceptance criteria and code quality standards, and either promotes it to `03_test` for testing or returns it to `00_refine` for rework with specific feedback.

## Usage

Use this skill when a task has been moved to `tasks/02_review/` by the doer and needs a quality check before testing. The reviewer will analyse the implementation against the task's own acceptance criteria and project-wide quality standards.

## Steps

1. **Fetch tasks for review**
   - List files in `02_review/`
   - If empty, notify the user and exit
   - If multiple tasks exist, present the list and ask which one to review

2. **Read the task specification**
   - Read the task file to understand:
     - The acceptance criteria
     - The implementation notes (files that were supposed to change)
     - Any dependencies

3. **Verify acceptance criteria**
   - For each acceptance criterion in the task file, check if it has been met
   - Validate with concrete evidence:
     - Read the modified files
     - Run the project (`python3 game.py` or equivalent) to observe behaviour
     - Check for edge cases mentioned in the task
   - Document which criteria pass and which fail

4. **Code quality review**
   - Check for:
     - **Consistency**: Does the code follow the same patterns as the rest of the project?
     - **Cleanliness**: No dead code, commented-out code, or debug logging left behind
     - **Regressions**: Does existing functionality still work? (check via `memory-bank/progress.md` what should still work)
     - **Naming**: Variables, functions, and classes follow the project's naming conventions
     - **Errors**: No Python runtime errors or import issues

5. **Decision**
   - **Pass**: All acceptance criteria met and no quality issues
     - Move the task file to `03_test`
   - **Fail**: One or more criteria not met, or quality issues found
     - Move the task file back to `00_refine`
     - Append a **Review Feedback** section to the task file detailing:
       - What failed and why
       - Specific, actionable guidance on what to fix

6. **Update progress**
   - Update `memory-bank/progress.md` to reflect the task's new status

## Review Checklist Template

When performing a review, systematically check:

- [ ] All acceptance criteria from the task file are satisfied
- [ ] No regressions in existing functionality
- [ ] No dead code, debug prints, or commented-out code
- [ ] Code follows project patterns and naming conventions
- [ ] The project runs without errors
- [ ] Edge cases from the task specification are handled

## Error Handling

- If a task cycles between review and refine more than 3 times, flag it to the user for manual intervention — something is fundamentally wrong with the task definition or approach
- If the task file is missing or corrupted, report to the user and do not silently create a new one
