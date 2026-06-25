# Pick the Best-Fitting Function

**Difficulty:** Medium  
**Course unit:** Unit 1.3 - Flow Control  
**Context:** Data Science (core assignment skill)

## Background

A scaled-down version of the assignment core: given a training series and several candidate series, choose the candidate that best matches by least squares. This combines a loop, a running minimum, and your SSE function.

## Task

Implement `best_fit(y_train, candidates)` where `candidates` is a dict {name: list_of_y}. Return the name whose list has the smallest sum of squared deviations from `y_train`.

## Requirements (graded)

- Returns the candidate name with the smallest SSE
- Correct after a candidate is removed / on random data

## Running the test

From inside this unit folder, run:

```bash
python ex_1_3_1_best_fit.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
