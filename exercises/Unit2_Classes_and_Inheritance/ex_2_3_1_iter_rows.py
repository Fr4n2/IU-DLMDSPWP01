'''Generator for Data Rows - see ex_2_3_1_iter_rows.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_2_3_1_*.py
'''

def iter_rows(xs, ys):
    # TODO (use yield)
    raise NotImplementedError

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("2.3.1", globals())
