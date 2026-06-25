# Vectorised SSE with NumPy

**Difficulty:** Medium  
**Course unit:** Unit 3.2 - Scientific Calculations  
**Context:** Data Science (core assignment skill)

## Background

NumPy lets you express the sum of squared errors without a Python loop, which is both clearer and far faster on large arrays.

## Task

Implement `sse_np(y_true, y_pred)` using NumPy (no explicit Python `for` loop) returning the sum of squared deviations. Inputs may be lists or NumPy arrays.

## Requirements (graded)

- Matches the reference on known and randomised inputs

## Running the test

From inside this unit folder, run:

```bash
python ex_3_2_1_sse_numpy.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
