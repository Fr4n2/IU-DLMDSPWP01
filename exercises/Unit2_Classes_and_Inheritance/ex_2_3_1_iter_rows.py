'''Generator for Data Rows - see ex_2_3_1_iter_rows.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_2_3_1_*.py
'''

def iter_rows(xs, ys):
    i = 0
    while i < len(xs):
        yield (xs[i], ys[i])
        i = i + 1

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("2.3.1", globals())
