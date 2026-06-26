'''Robust CSV Loading - see ex_4_2_1_safe_load.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_4_2_1_*.py
'''

def safe_load(path):
    data = []
    try:
        with open(path, "r") as file:
            for line in file:
                try:
                    # print(line)
                    columns = line.split(",")
                    data.append((float(columns[0]), float(columns[1])))
                except Exception as e:
                    print(e)
                    continue
    except FileNotFoundError as fnfe:
         print(fnfe)
    
    return data


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("4.2.1", globals())
