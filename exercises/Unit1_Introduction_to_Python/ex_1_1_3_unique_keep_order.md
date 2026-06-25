# Unique Names, Order Preserved

**Difficulty:** Easy  
**Course unit:** Unit 1.1 - Data Structures  
**Context:** Data Science

## Background

When handling column names of a dataset you often need to drop duplicates while keeping the original order. A plain `set` loses order, so you must combine a `set` (for fast membership tests) with a `list` (for order).

## Task

Implement `unique_keep_order(names)` that returns a new list with duplicates removed, keeping the first occurrence of each element in its original position.

## Requirements (graded)

- Correct on basic and empty inputs
- Preserves first-seen order on randomised inputs

## Running the test

From inside this unit folder, run:

```bash
python ex_1_1_3_unique_keep_order.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
