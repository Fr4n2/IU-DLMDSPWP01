# User-Defined Exception and sqrt(2) Rule

**Difficulty:** Hard  
**Course unit:** Unit 4.3 - User-Defined Exceptions  
**Context:** Data Science (core assignment skill)

## Background

The assignment maps a test point to an ideal function only if its deviation stays within the largest training deviation times sqrt(2); otherwise it must signal that no function fits. That signal is a user-defined exception.

## Task

Define an exception class `NoMatchingFunctionError(Exception)`. Implement `assign(point_dev, max_train_dev)` that returns the string "matched" when `point_dev <= max_train_dev * sqrt(2)`, and otherwise raises `NoMatchingFunctionError`.

## Requirements (graded)

- Maps within the sqrt(2) tolerance and raises beyond it
- `NoMatchingFunctionError` subclasses `Exception`

## Running the test

From inside this unit folder, run:

```bash
python ex_4_3_1_no_matching_function.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
