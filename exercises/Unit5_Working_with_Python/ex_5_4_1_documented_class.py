'''A Fully Documented Class - see ex_5_4_1_documented_class.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_5_4_1_*.py
'''
import math

class Statistics:
    """
    Provides basic statistic methods
    """
    def __init__(self, values):
        self.values = values

    def mean(self):
        """
        Calculate the mean of the own values
        """
        average = sum(self.values) / len(self.values)
        return average

    def std(self):
        """
        Calculate the standard deviation of the own values
        """
        mean = self.mean()
        squared_deviations = []
        for value in self.values:
            deviation = value - mean
            squared_deviations.append(deviation**2)
        variance = sum(squared_deviations) / (len(self.values)+0)
        std = math.sqrt(variance)
        return std
        



if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("5.4.1", globals())
