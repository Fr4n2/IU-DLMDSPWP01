# Most Common Labels

**Difficulty:** Easy  
**Course unit:** Unit 3.1 - Standard Python Library  
**Context:** Data Science

## Background

`collections.Counter` is a workhorse for frequency analysis. `most_common(n)` returns the n highest-frequency items.

## Task

Implement `top_labels(labels, n=2)` returning the `n` most common labels as a list of `(label, count)` tuples, highest count first.

## Requirements (graded)

- Returns the n most common (label, count) pairs

## Running the test

From inside this unit folder, run:

```bash
python ex_3_1_1_top_labels.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
