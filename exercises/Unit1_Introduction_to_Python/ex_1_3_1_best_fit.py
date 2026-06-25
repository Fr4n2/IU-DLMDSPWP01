'''Pick the Best-Fitting Function - see ex_1_3_1_best_fit.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_1_3_1_*.py
'''

def best_fit(y_train, candidates):
    # TODO
    raise NotImplementedError

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("1.3.1", globals())
