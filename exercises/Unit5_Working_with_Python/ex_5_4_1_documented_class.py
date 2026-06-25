'''A Fully Documented Class - see ex_5_4_1_documented_class.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_5_4_1_*.py
'''

class Statistics:
    # TODO: add a class docstring
    def __init__(self, values):
        self.values = values

    def mean(self):
        # TODO: add a docstring and implement
        raise NotImplementedError

    def std(self):
        # TODO: add a docstring and implement
        raise NotImplementedError

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("5.4.1", globals())
