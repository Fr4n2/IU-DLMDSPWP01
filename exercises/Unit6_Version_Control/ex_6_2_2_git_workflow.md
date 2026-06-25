# The Assignment's Git Workflow

**Difficulty:** Medium  
**Course unit:** Unit 6.2 - Version Control With Git  
**Context:** Engineering (assignment bonus task)

## Background

The assignment's bonus question asks for the Git commands to clone a shared develop branch, contribute a new function, and have it merged after review. Here you encode that sequence as data so it can be checked automatically.

## Task

Fill the list `GIT_COMMANDS` with the shell commands, in order, that you would run: clone the repository, switch to the develop branch, stage your change, commit it, and push it. (The Pull Request and merge happen in the web UI afterwards.)

## Requirements (graded)

- Contains git clone, add, commit and push commands in a sensible order

## Running the test

From inside this unit folder, run:

```bash
python ex_6_2_2_git_workflow.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
