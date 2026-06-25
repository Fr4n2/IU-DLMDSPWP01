'''DataSet Base Class and Subclasses - see ex_2_2_1_dataset_oop.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_2_2_1_*.py
'''

class DataSet:
    def __init__(self, x, y):
        # TODO
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def sse(self, other):
        raise NotImplementedError


class TrainingData(DataSet):
    pass


class IdealFunction(DataSet):
    def __init__(self, x, y, name=""):
        # TODO
        raise NotImplementedError

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("2.2.1", globals())
