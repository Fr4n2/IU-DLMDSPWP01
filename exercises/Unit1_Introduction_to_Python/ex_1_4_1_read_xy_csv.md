# Read an x-y CSV Without Pandas

**Difficulty:** Medium  
**Course unit:** Unit 1.4 - Input / Output  
**Context:** Data Science (core assignment skill)

## Background

Before reaching for Pandas, you should be able to parse a simple CSV by hand. The assignment data is always x-y pairs with a header row.

## Task

Implement `read_xy_csv(path)` that opens a CSV file with header `x,y` and returns a list of `(float, float)` tuples, one per data row (the header is not included).

## Requirements (graded)

- Returns a list of (float, float) tuples with the header removed

## Running the test

From inside this unit folder, run:

```bash
python ex_1_4_1_read_xy_csv.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
