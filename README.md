# Olist Marketplace Analytics Pipeline

> One-line summary: an end-to-end analytics pipeline on Brazilian e-commerce data (Olist), covering delivery performance, customer retention and revenue.

## Business problem
Write 3 to 4 sentences: who would use this analysis and what decisions it supports.

## Business questions
1. Which product categories drive revenue, and how has this changed over time?
2. Which regions and sellers have the worst delivery delays?
3. What is the repeat-purchase rate, and what does cohort retention look like?
4. Does late delivery hurt review scores, and by how much?
5. Which customer segments (RFM) are most valuable?

## Architecture
_Add an architecture diagram in `docs/` and embed it here (raw CSV -> Python ETL -> SQL star schema -> dashboard)._

## Tech stack
Python (pandas, SQLAlchemy), PostgreSQL / SQLite, SQL (CTEs, window functions), Power BI / Tableau / Streamlit, pytest, Docker (planned).

## Project structure
```
data/raw/        raw Olist CSVs (not committed)
data/processed/  cleaned outputs (not committed)
src/             pipeline code (config, extract, clean, load, run_pipeline)
sql/             numbered, commented analysis queries
notebooks/       EDA notebooks
tests/           unit tests
dashboard/       dashboard files and screenshots
docs/            diagrams, ERD, data dictionary
```

## Setup
```bash
git clone <your-repo-url>
cd olist-marketplace-analytics
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env              # Windows: copy .env.example .env
```

## Get the data
Download "Brazilian E-Commerce Public Dataset by Olist" from Kaggle and place the 9 CSV files in `data/raw/`.

## Run the pipeline
```bash
python -m src.run_pipeline
```

## Key findings
_Fill in after analysis, with real numbers and recommendations._

## Data quality and cleaning decisions
_Document each decision and why._

## Limitations and future work
_Be honest about what this does not cover._

## Author
Vindhya Chandrashekhar | [LinkedIn](https://linkedin.com/in/vindhya-chandrashekhar20) | [GitHub](https://github.com/vindhyac20)
