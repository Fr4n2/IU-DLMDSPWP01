'''Read an x-y CSV Without Pandas - see ex_1_4_1_read_xy_csv.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_1_4_1_*.py
'''

def read_xy_csv(path):
    data = []
    with open(path, "r") as file:
        for line in file:
            columns = line.split(",")
            if not columns[0] == 'x' and not columns[1] == 'y\n':
                    data.append((float(columns[0]), float(columns[1])))
    print(data)
    return data


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("1.4.1", globals())
