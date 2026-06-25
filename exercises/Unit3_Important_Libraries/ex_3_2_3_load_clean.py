'''Load CSV and Handle NaN with Pandas - see ex_3_2_3_load_clean.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_3_2_3_*.py
'''

import pandas as pd


def load_clean(path):
    # TODO
    raise NotImplementedError

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("3.2.3", globals())
