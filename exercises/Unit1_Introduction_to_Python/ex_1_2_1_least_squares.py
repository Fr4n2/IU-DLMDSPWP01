'''Least-Squares Error - see ex_1_2_1_least_squares.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_1_2_1_*.py
'''

def sum_squared_error(y_true, y_pred):
    # TODO
    raise NotImplementedError

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("1.2.1", globals())
