'''Read an x-y CSV Without Pandas - see ex_1_4_1_read_xy_csv.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_1_4_1_*.py
'''

def read_xy_csv(path):
    # TODO
    raise NotImplementedError

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("1.4.1", globals())
