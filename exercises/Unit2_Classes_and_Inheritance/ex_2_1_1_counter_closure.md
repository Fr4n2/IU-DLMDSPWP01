# Counter via Closure

**Difficulty:** Medium  
**Course unit:** Unit 2.1 - Scopes and Namespaces  
**Context:** Data Science

## Background

Closures capture variables from an enclosing scope. To modify such a captured variable you need the `nonlocal` keyword. Each closure keeps its own independent state.

## Task

Implement `make_counter(start=0)` that returns a function. Each call to that returned function increments an internal counter by 1 and returns the new value. The first returned value is `start + 1`.

## Requirements (graded)

- Counts up on each call
- `start` sets the base; separate counters are independent

## Running the test

From inside this unit folder, run:

```bash
python ex_2_1_1_counter_closure.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
