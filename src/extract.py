"""Extract step: read the raw Olist CSV files into pandas DataFrames."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.config import RAW_DIR, get_logger

logger = get_logger(__name__)

# table name -> expected file name in data/raw/
EXPECTED_FILES: dict[str, str] = {
    "customers": "olist_customers_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "order_payments": "olist_order_payments_dataset.csv",
    "order_reviews": "olist_order_reviews_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "category_translation": "product_category_name_translation.csv",
}


def load_raw_tables(raw_dir: Path = RAW_DIR) -> dict[str, pd.DataFrame]:
    """Load every expected Olist CSV and return them keyed by table name.

    Raises:
        FileNotFoundError: if any expected file is missing from ``raw_dir``.
    """
    missing = [f for f in EXPECTED_FILES.values() if not (raw_dir / f).exists()]
    if missing:
        raise FileNotFoundError(
            f"Missing files in {raw_dir}: {missing}. See README for download steps."
        )

    tables: dict[str, pd.DataFrame] = {}
    for name, filename in EXPECTED_FILES.items():
        df = pd.read_csv(raw_dir / filename)
        logger.info("Loaded %-22s %8d rows, %2d columns", name, df.shape[0], df.shape[1])
        tables[name] = df
    return tables
