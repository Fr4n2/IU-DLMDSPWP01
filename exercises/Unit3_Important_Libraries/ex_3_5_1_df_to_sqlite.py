'''DataFrame to SQLite via SQLAlchemy - see ex_3_5_1_df_to_sqlite.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_3_5_1_*.py
'''

import pandas as pd
from sqlalchemy import create_engine


def df_to_sqlite(df, table, db_url="sqlite:///out.db"):
    # TODO
    raise NotImplementedError

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("3.5.1", globals())
