# Tic-Tac-Toe Board

**Difficulty:** Easy to Medium  
**Course unit:** Unit 1.1 - Data Structures  
**Context:** Game development

## Background

Game state is often stored in nested data structures. A 3x3 board is a list of three rows, each a list of three cells. This exercise practises nested lists, indexing, and the difference between mutating an object in place and creating a new one.

## Task

Implement three functions:
- `make_board()` returns a fresh 3x3 board with every cell set to a single space `" "`.
- `set_cell(board, row, col, mark)` places `mark` at the given position, modifying the board in place.
- `is_full(board)` returns `True` if no cell still holds a space, else `False`.

## Requirements (graded)

- `make_board()` creates an empty 3x3 board
- `set_cell` places marks at the correct position
- `is_full` distinguishes empty from full boards

## Running the test

From inside this unit folder, run:

```bash
python ex_1_1_2_tic_tac_toe.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
