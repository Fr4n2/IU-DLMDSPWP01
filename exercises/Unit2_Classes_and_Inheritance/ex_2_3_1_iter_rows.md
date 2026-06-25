# Generator for Data Rows

**Difficulty:** Medium  
**Course unit:** Unit 2.3 - Iterators and Generators  
**Context:** Data Science (core assignment skill)

## Background

Generators yield values lazily and are ideal for reading test data line by line without loading everything into memory - exactly the access pattern the assignment uses for the test dataset.

## Task

Implement `iter_rows(xs, ys)` as a generator (use `yield`) that produces `(x, y)` tuples in order.

## Requirements (graded)

- Is a real generator and yields (x,y) tuples in order

## Running the test

From inside this unit folder, run:

```bash
python ex_2_3_1_iter_rows.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
