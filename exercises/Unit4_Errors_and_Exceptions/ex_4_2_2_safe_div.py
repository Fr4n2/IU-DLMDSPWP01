'''Division with Exception Info - see ex_4_2_2_safe_div.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_4_2_2_*.py
'''

import sys


def safe_div(a, b):
    # TODO (use try/except)
    raise NotImplementedError

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("4.2.2", globals())
