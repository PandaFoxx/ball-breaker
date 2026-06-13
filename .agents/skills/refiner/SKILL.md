---
name: refiner
description: Picks a raw task from todo.md, analyses it, breaks it down into clear implementation steps, and saves a refined task file to 00_refine.
---

# refiner

The refiner skill bridges the gap between the rough todo list (`todo.md`) and actionable implementation tasks. It takes a raw requirement, removes ambiguity, decomposes it into concrete sub-steps, and saves a structured task file ready for a doer to execute.

## Usage

Use this skill when there are items in `todo.md` that need to be broken into precise, implementable tasks. The refiner will analyse each item, ask clarifying questions if needed, and produce a polished task file in `tasks/00_refine/`.

## Steps

1. **Read the source**
   - Read `todo.md`
   - Identify the "todo" section items that have not yet been refined
   - Present the list of unrefined items to the user

2. **Select a task to refine**
   - Ask the user which item they want refined
   - Read the existing task files in `tasks/00_refine/` to avoid duplicating work

3. **Analyse and decompose**
   - For the selected item, break it down into concrete sub-tasks
   - Consider:
     - Dependencies (does another task need to be done first?)
     - Acceptance criteria (how do we know it's done?)
     - Edge cases and failure modes
     - Required changes to specific files
   - If the item is too vague, propose a concrete interpretation to the user

4. **Create the refined task file**
   - Save the breakdown to `tasks/00_refine/`
   - Name format: `YYYYMMDDHHMM-short-descriptive-name.md`
     - Example: `202606142355-add-start-screen.md`
   - The file must include:
     - **Title**: A clear one-line summary
     - **Description**: What needs to be done and why
     - **Acceptance Criteria**: Checkable conditions for completion
     - **Implementation Notes**: Files to modify, technical approach
     - **Dependencies**: Any prerequisite tasks
     - **Sub-tasks**: Ordered list of actionable steps

5. **Clean up**
   - Remove the refined item from the "todo" list in `todo.md`
   - Update `memory-bank/progress.md` to reflect the new task being in the refine queue

## Task File Template

```markdown
# Title: [Short one-line summary]

## Description
[What needs to be done and why]

## Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]

## Implementation Notes
- Files to modify: [file paths]
- Technical approach: [brief description]

## Dependencies
- [ ] [Prerequisite task]

## Sub-tasks
- [ ] [Step 1]
- [ ] [Step 2]
```

## Error Handling

- If `todo.md` has no unrefined items, notify the user and exit
- If an item is already covered by an existing refined task file, skip it and report the overlap
