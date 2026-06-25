'''User-Defined Exception and sqrt(2) Rule - see ex_4_3_1_no_matching_function.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_4_3_1_*.py
'''

import math


class NoMatchingFunctionError(Exception):
    pass


def assign(point_dev, max_train_dev):
    # TODO
    raise NotImplementedError

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("4.3.1", globals())
