'''Most Common Labels - see ex_3_1_1_top_labels.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_3_1_1_*.py
'''

from collections import Counter

def top_labels(labels, n=2):
    counter = Counter(labels)
    list_of_top_labels = counter.most_common(n)
    # list_of_top_labels = []
    # for label, count in counter.items():
    #     print(count)
    #     if count >= n:
    #         list_of_top_labels.append((label, count))
    return list_of_top_labels

    

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("3.1.1", globals())
