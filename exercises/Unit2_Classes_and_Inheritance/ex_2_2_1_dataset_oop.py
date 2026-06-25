'''DataSet Base Class and Subclasses - see ex_2_2_1_dataset_oop.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_2_2_1_*.py
'''

class DataSet:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return len(self.x)

    def sse(self, other):
        if len(self) != len(other):
            raise ValueError("Different length of input values")
        sum_squared_error = 0.0
        
        for i in range(len(self.y)):
            sum_squared_error = sum_squared_error + (self.y[i] - other.y[i])**2
        return sum_squared_error
        


class TrainingData(DataSet):
    pass


class IdealFunction(DataSet):
    def __init__(self, x, y, name=""):
        super().__init__(x,y)
        self.name = name
        
    def __repr__(self):
        return self.name

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("2.2.1", globals())
