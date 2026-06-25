'''Counter via Closure - see ex_2_1_1_counter_closure.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_2_1_1_*.py
'''


def make_counter(start=0):
    counter = start
    
    def increment_counter():
        nonlocal counter
        counter = counter+1
        return counter
    return increment_counter

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("2.1.1", globals())
