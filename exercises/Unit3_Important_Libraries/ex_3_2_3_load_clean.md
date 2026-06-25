# Load CSV and Handle NaN with Pandas

**Difficulty:** Medium  
**Course unit:** Unit 3.2 - Scientific Calculations  
**Context:** Data Science (core assignment skill)

## Background

Real datasets have gaps. Pandas reads CSVs and offers `fillna` to replace missing values; a common strategy is the column mean.

## Task

Implement `load_clean(path)` that reads a CSV with `pd.read_csv`, replaces any NaN in column `y` with the mean of column `y`, and returns the cleaned DataFrame.

## Requirements (graded)

- Loads the CSV and leaves no NaN in y
- Fills missing y-values with the column mean

## Running the test

From inside this unit folder, run:

```bash
python ex_3_2_3_load_clean.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
