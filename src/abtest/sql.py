"""Run the queries in sql/ against in-memory DuckDB (provided)."""
from __future__ import annotations

from pathlib import Path

import duckdb
import pandas as pd

SQL_DIR = Path(__file__).resolve().parents[2] / "sql"


def run_sql(name: str, users: pd.DataFrame, events: pd.DataFrame) -> pd.DataFrame:
    """Execute sql/<name>.sql with tables `users` and `events` available."""
    query = (SQL_DIR / f"{name}.sql").read_text()
    con = duckdb.connect()
    con.register("users", users)
    con.register("events", events)
    return con.execute(query).df()
