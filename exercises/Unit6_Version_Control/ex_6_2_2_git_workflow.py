'''The Assignment's Git Workflow - see ex_6_2_2_git_workflow.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_6_2_2_*.py
'''

GIT_COMMANDS = [
    # "git clone <repo-url>",
    # ... fill in the rest in order ...
]

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("6.2.2", globals())
