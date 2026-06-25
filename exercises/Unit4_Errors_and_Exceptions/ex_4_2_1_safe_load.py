'''Robust CSV Loading - see ex_4_2_1_safe_load.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_4_2_1_*.py
'''

def safe_load(path):
    # TODO (use try/except)
    raise NotImplementedError

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("4.2.1", globals())
