# Robust CSV Loading

**Difficulty:** Medium  
**Course unit:** Unit 4.2 - Handling and Raising Exceptions  
**Context:** Data Science (core assignment skill)

## Background

Production code must survive bad input. Here you guard file access and parsing with standard exception handling.

## Task

Implement `safe_load(path)` returning a list of `(float, float)` tuples. If the file does not exist, return an empty list. If a data line cannot be parsed into two floats, skip that line and continue.

## Requirements (graded)

- Returns an empty list when the file is missing
- Skips malformed lines and keeps the valid (x, y) rows

## Running the test

From inside this unit folder, run:

```bash
python ex_4_2_1_safe_load.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
