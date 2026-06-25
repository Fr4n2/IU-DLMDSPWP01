# A Function with a Passing Doctest

**Difficulty:** Easy to Medium  
**Course unit:** Unit 5.4 - Documenting Code  
**Context:** Data Science

## Background

Doctests embed runnable examples in a docstring; the testing tools execute them and verify the output. This is documentation and a test at once.

## Task

Implement `square(x)` with a docstring that contains at least one doctest example (a line starting with `>>>`). The example must pass and the function must be correct.

## Requirements (graded)

- The docstring contains a doctest example that passes
- The function returns the square of its input

## Running the test

From inside this unit folder, run:

```bash
python ex_5_4_2_doctest.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
