'''Vectorised SSE with NumPy - see ex_3_2_1_sse_numpy.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_3_2_1_*.py
'''

import numpy as np


def sse_np(y_true, y_pred):
    # TODO (vectorised, no for-loop)
    raise NotImplementedError

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("3.2.1", globals())
