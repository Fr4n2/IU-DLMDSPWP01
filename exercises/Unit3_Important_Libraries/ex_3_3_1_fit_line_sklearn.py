'''Linear Regression with scikit-learn - see ex_3_3_1_fit_line_sklearn.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_3_3_1_*.py
'''

from sklearn.linear_model import LinearRegression


def fit_line(x, y):
    model = LinearRegression()
    model.fit(x, y)

    print((model.coef_[0], model.intercept_))
          
    return (model.coef_[0], model.intercept_)

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("3.3.1", globals())
