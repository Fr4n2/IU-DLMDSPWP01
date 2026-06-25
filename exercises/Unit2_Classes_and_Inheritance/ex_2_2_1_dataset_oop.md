# DataSet Base Class and Subclasses

**Difficulty:** Hard  
**Course unit:** Unit 2.2 - Classes and Inheritance  
**Context:** Data Science (core assignment skill)

## Background

The assignment requires a sensible object-oriented design with at least one inheritance. This builds exactly that skeleton: a base class for x-y data and two specialised subclasses.

## Task

Implement a base class `DataSet` with `__init__(self, x, y)` storing two lists, a `__len__` returning the number of points, and `sse(self, other)` returning the sum of squared differences between its own y-values and another DataSet's y-values. Add `TrainingData(DataSet)` and `IdealFunction(DataSet)`. `IdealFunction.__init__` also takes a keyword `name`, and `IdealFunction` overrides `__repr__` to include that name.

## Requirements (graded)

- `__len__` returns the number of points
- `sse` compares y-values correctly
- Both subclasses inherit from `DataSet`
- `IdealFunction`'s repr includes its name

## Running the test

From inside this unit folder, run:

```bash
python ex_2_2_1_dataset_oop.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
