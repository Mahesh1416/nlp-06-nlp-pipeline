"""
src/nlp/config_case.py - Module 5 Configuration
(COPY AND MODIFY THIS FILE - do not edit the original)

Stores configuration values for the web document EVTL pipeline.
Source: arXiv abstract page for "Agents of Chaos" (2602.20021)

Purpose

  Store configuration values.

Analytical Questions

- What web page URL should be used as the data source?
- Where should raw and processed data be stored?

Notes

Following our process, do NOT edit this _case file directly,
keep it as a working example.

In your custom project,copy this _case.py file and
append with _yourname.py instead.

Then edit your copied Python file to change:
- PAGE_URL (source of the HTML web page document),
- customize your output file name.
"""

from pathlib import Path

# ============================================================
# API CONFIGURATION
# ============================================================

# Updated arXiv URL
PAGE_URL: str = "https://arxiv.org/abs/2603.23289"

# HTTP headers (good practice for web requests)
HTTP_REQUEST_HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (educational-use; web-mining-course)"
}

# ============================================================
# PATH CONFIGURATION
# ============================================================

# Always resolve project root reliably (DO NOT use Path.cwd())
ROOT_PATH: Path = Path(__file__).resolve().parents[2]

# Data directories
DATA_PATH: Path = ROOT_PATH / "data"
RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"

# Output files (custom names)
RAW_HTML_PATH: Path = RAW_PATH / "mahesh_raw.html"
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "mahesh_processed.csv"
