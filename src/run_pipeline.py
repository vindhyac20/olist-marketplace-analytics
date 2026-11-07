"""Run the full pipeline: extract -> clean -> load.

Usage (from the project root):
    python -m src.run_pipeline
"""
from __future__ import annotations

from src.config import get_logger
from src.extract import load_raw_tables

logger = get_logger(__name__)


def main() -> None:
    logger.info("Pipeline started")
    tables = load_raw_tables()
    logger.info("Extracted %d tables", len(tables))
    # TODO (Day 6): clean and merge tables  -> src/clean.py
    # TODO (Day 3): load into the database -> src/load.py
    logger.info("Pipeline finished")


if __name__ == "__main__":
    main()
