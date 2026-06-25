'''Pick the Best-Fitting Function - see ex_1_3_1_best_fit.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_1_3_1_*.py
'''

def best_fit(y_train, candidates):
    solution = ""
    smallest_squared_error = float('inf')
    for name, series in candidates.items():
        error_size = sum_squared_error(y_train, series)
        if error_size < smallest_squared_error:
            solution = name
            smallest_squared_error = error_size
    return solution

    

def sum_squared_error(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("Different length of input values")
    sum_squared_error = 0.0
    
    for i in range(len(y_true)):
        sum_squared_error = sum_squared_error + (y_true[i] - y_pred[i])**2

    return sum_squared_error   

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("1.3.1", globals())
