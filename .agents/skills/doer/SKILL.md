---
name: doer
description: Executes a refined task from the refine queue — picks a task, works on it, pushes it to review.
---

# doer

The doer skill is the execution engine of the workflow. It picks a refined task from `00_refine/`, moves it to `01_busy/`, implements the changes, and pushes it to `02_review/` for peer review.

## Usage

Use this skill when you're ready to implement a task that has already been refined and saved to `tasks/00_refine/`. The doer will present available tasks, let you choose one (or pick randomly), then execute the work.

## Steps

1. **Fetch available tasks**
   - List files in `00_refine/`
   - If empty, notify the user that no tasks are ready and exit

2. **Select a task**
   - Present the list of task files to the user
   - Ask which one to work on, or if they want a random pick
   - If random is chosen, pick one uniformly at random

3. **Claim the task**
   - Move the selected task file to `01_busy/`
   - Read the task file to understand the full requirements

4. **Implement the task**
   - Work on the task, making all necessary code/file changes
   - Update `memory-bank/progress.md` as you go:
     - Mark in-progress items as `[ ]`
     - Mark completed items as `[x]`
     - Update "Known Issues" and "What Works" sections as needed

5. **Submit for review**
   - Move the task file from `01_busy/` to `02_review/`
   - Confirm completion to the user with a summary of what was done

## Error Handling

- If multiple tasks exist in `00_refine/`, do **not** batch-execute — only one at a time
- If the task file contains ambiguous or incomplete requirements, flag it and send back to `00_refine/` instead of implementing
- If implementation reveals the task is too large, notify the user and suggest splitting it
