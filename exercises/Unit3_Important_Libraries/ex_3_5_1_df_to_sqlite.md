# DataFrame to SQLite via SQLAlchemy

**Difficulty:** Medium  
**Course unit:** Unit 3.5 - Accessing Databases  
**Context:** Data Science (core assignment skill)

## Background

The assignment stores its tables in a SQLite database, ideally through SQLAlchemy. The quickest reliable path is an engine plus DataFrame.to_sql.

## Task

Implement `df_to_sqlite(df, table, db_url="sqlite:///out.db")` that creates a SQLAlchemy engine for `db_url` and writes `df` to a table named `table` (replace if it exists).

## Requirements (graded)

- Writes the DataFrame so it can be read back identically

## Running the test

From inside this unit folder, run:

```bash
python ex_3_5_1_df_to_sqlite.py
```

You will see one PASS/FAIL line per requirement and a final score. The expected values live in `grader.py` in encoded form, so you get feedback on *whether* a requirement is met without seeing the answer.
