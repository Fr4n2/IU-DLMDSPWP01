'''Unique Names, Order Preserved - see ex_1_1_3_unique_keep_order.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_1_1_3_*.py
'''

def unique_keep_order(names):
    unique_list = []
    unique_set = set() # searching in Set is faster with O(n), instead of searching the list with O(n²)
    for name in names:
        if name not in unique_set:
            unique_list.append(name)
            unique_set.add(name)
    return unique_list


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("1.1.3", globals())
