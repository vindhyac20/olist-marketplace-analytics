"""Helpers for inspecting and sanity-checking DataFrames."""
from __future__ import annotations

import pandas as pd


def profile_table(df: pd.DataFrame) -> pd.DataFrame:
    """Return one row per column with dtype, null count, null percent and unique count."""
    return pd.DataFrame(
        {
            "dtype": df.dtypes.astype(str),
            "nulls": df.isna().sum(),
            "null_pct": (df.isna().mean() * 100).round(2),
            "unique": df.nunique(),
        }
    )


def overview(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Return one row per table with rows, columns, duplicate rows and memory use."""
    rows = []
    for name, df in tables.items():
        rows.append(
            {
                "table": name,
                "rows": df.shape[0],
                "columns": df.shape[1],
                "duplicate_rows": int(df.duplicated().sum()),
                "memory_mb": round(df.memory_usage(deep=True).sum() / 1024**2, 2),
            }
        )
    return pd.DataFrame(rows).set_index("table")


def missing_keys(
    child: pd.DataFrame, child_col: str, parent: pd.DataFrame, parent_col: str
) -> int:
    """Count child rows whose key value does not exist in the parent table."""
    return int((~child[child_col].isin(parent[parent_col])).sum())
