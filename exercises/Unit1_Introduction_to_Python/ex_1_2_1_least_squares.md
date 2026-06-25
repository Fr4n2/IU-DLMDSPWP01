# Least-Squares Error

**Difficulty:** Medium  
**Course unit:** Unit 1.2 - Functions  
**Context:** Data Science (core assignment skill)

## Background

The assignment selects ideal functions by minimising the sum of squared deviations (least squares). This is the most important numeric primitive in the whole project, written here in plain Python.

## Task

Implement `sum_squared_error(y_true, y_pred)` returning the sum of (y_true[i] - y_pred[i])**2 over all i. If the two sequences differ in length, raise a `ValueError`.

## Requirements (graded)

- Correct on known cases
- Correct on randomised inputs
- Raises `ValueError` when the inputs differ in length

## Running the test

From inside this unit folder, run:

```bash
python ex_1_2_1_least_squares.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
