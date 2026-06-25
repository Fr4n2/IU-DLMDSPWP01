'''A Function with a Passing Doctest - see ex_5_4_2_doctest.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_5_4_2_*.py
'''

def square(x):
    """Return the square of x.

    Add a doctest example below, e.g. >>> square(3) returning 9.
    """
    # TODO
    raise NotImplementedError

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("5.4.2", globals())
