# Linear Regression with scikit-learn

**Difficulty:** Medium  
**Course unit:** Unit 3.3 - Machine Learning Libraries  
**Context:** Machine Learning

## Background

scikit-learn's `LinearRegression` exposes a clean fit/predict API. After fitting, the slope is in `coef_` and the offset in `intercept_`.

## Task

Implement `fit_line(x, y)` that fits a `LinearRegression` on the data and returns `(slope, intercept)`. `x` is a 2D array of shape (n, 1).

## Requirements (graded)

- Returns the correct slope and intercept on a clean line

## Running the test

From inside this unit folder, run:

```bash
python ex_3_3_1_fit_line_sklearn.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
