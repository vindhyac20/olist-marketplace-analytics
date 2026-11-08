import pandas as pd

from src.profiling import missing_keys, overview, profile_table


def test_profile_table_counts_nulls_and_unique():
    df = pd.DataFrame({"a": [1, None, 3], "b": ["x", "y", "y"]})
    profile = profile_table(df)
    assert profile.loc["a", "nulls"] == 1
    assert profile.loc["b", "unique"] == 2


def test_overview_counts_duplicate_rows():
    df = pd.DataFrame({"a": [1, 1, 2]})
    result = overview({"t": df})
    assert result.loc["t", "rows"] == 3
    assert result.loc["t", "duplicate_rows"] == 1


def test_missing_keys_counts_orphans():
    child = pd.DataFrame({"k": [1, 2, 3]})
    parent = pd.DataFrame({"id": [1, 2]})
    assert missing_keys(child, "k", parent, "id") == 1
