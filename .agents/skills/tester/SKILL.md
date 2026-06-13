---
name: tester
description: Tests completed implementations against functional requirements, either sending back for rework or marking as done.
---

# tester

The tester skill is the final validation step of the workflow. It picks a reviewed task from `03_test/`, runs functional tests on the implementation, and either sends it back to `01_busy/` for rework or moves it to `04_done/` upon successful completion.

## Usage

Use this skill when a task has passed review and been moved to `tasks/03_test/`. The tester will verify the implementation works correctly in the running application, exercising the feature end-to-end.

## Steps

1. **Fetch task for testing**
   - List files in `tasks/03_test/`
   - If empty, notify the user and exit
   - If multiple tasks exist, present the list and ask which one to test

2. **Read the task specification**
   - Read the task file to understand:
     - The feature being implemented
     - The acceptance criteria
     - Any edge cases documented in sub-tasks

3. **Run the application**
   - Execute `python3 game.py`
   - Observe the behaviour related to the task

4. **Execute test scenarios**
   - For each acceptance criterion, perform a manual test:
     - **Happy path**: Does the feature work correctly under normal conditions?
     - **Edge cases**: What happens at boundaries (e.g., screen edges, zero lives, max speed)?
     - **Failure modes**: Does it degrade gracefully (e.g., missing assets, invalid state)?
   - If the project has automated tests, run those as well
   - Document which scenarios pass and which fail

5. **Check for regressions**
   - Verify that existing documented functionality (from `memory-bank/progress.md` "What Works" section) still behaves correctly
   - If the task changed shared code, test related features too

6. **Decision**
   - **Pass**: All acceptance criteria met, no regressions, edge cases handled
     - Move the task file to `tasks/04_done/`
     - Update `memory-bank/progress.md`:
       - Move the completed item from "What's Left to Build" to "What Works"
       - Remove any resolved "Known Issues"
   - **Fail**: One or more criteria not met, regression found, or edge case broken
     - Move the task file back to `tasks/01_busy/`
     - Append a **Test Feedback** section to the task file detailing:
       - What failed and under what conditions
       - Steps to reproduce the failure
       - What a passing test should look like

7. **Report results**
   - Summarise to the user what was tested, what passed, what failed (if anything)
   - If passed, confirm the feature is now complete and done

## Test Criteria Checklist

When testing, systematically check:

- [ ] Feature works in normal operation (happy path)
- [ ] Edge cases are handled (boundaries, limits, empty states)
- [ ] Failure modes are graceful (no crashes, informative messages)
- [ ] No regressions in previously working features
- [ ] The application does not crash or produce errors in the terminal
- [ ] The feature feels intuitive and matches the user's expectation

## Error Handling

- If the application crashes on launch, report immediately — do not attempt to test further
- If a task cycles between tester and doer more than 3 times, flag to the user for manual intervention
- If the task file is missing or corrupted, report to the user and do not proceed
- If the feature cannot be tested manually (e.g., it's code-only with no visual impact), verify through code inspection and explain the approach
