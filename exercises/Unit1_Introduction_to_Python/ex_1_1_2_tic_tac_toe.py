'''Tic-Tac-Toe Board - see ex_1_1_2_tic_tac_toe.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_1_1_2_*.py
'''

def make_board():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    return board


def set_cell(board, row, col, mark):
    board[row][col] = mark


def is_full(board):
    for row in board:
        for column in row:
            if column == ' ':
                return False
    return True

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("1.1.2", globals())
