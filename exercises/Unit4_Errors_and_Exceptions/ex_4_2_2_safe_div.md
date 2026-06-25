# Division with Exception Info

**Difficulty:** Easy  
**Course unit:** Unit 4.2 - Handling and Raising Exceptions  
**Context:** Data Science

## Background

Catching an exception lets you report what went wrong instead of crashing. Python exposes the active exception type via `sys.exc_info()`.

## Task

Implement `safe_div(a, b)` that returns `a / b`, but on a zero divisor returns a string containing the exception type name (for example, contains "ZeroDivisionError").

## Requirements (graded)

- Normal division works; zero divisor reports the exception type as a string

## Running the test

From inside this unit folder, run:

```bash
python ex_4_2_2_safe_div.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
