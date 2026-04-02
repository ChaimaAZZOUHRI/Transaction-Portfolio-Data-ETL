import logging
import re
from pathlib import Path

import pandas as pd


def setup_logger(log_file: str, logger_name: str | None = None) -> logging.Logger:
    """
    Create and return a logger that writes both to a file and to the console.
    """
    logger = logging.getLogger(logger_name or __name__)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers if the function is called more than once
    if logger.handlers:
        return logger

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8") 
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


def parse_mixed_date(value):
    """
    Parse dates that may appear in different formats:
    - YYYY-MM-DD HH:MM:SS
    - DD/MM/YYYY HH:MM
    Returns pd.NaT when parsing fails.
    """
    if pd.isna(value):
        return pd.NaT

    value = str(value).strip()

    try:
        if "/" in value:
            return pd.to_datetime(value, dayfirst=True, errors="coerce")
        return pd.to_datetime(value, errors="coerce")
    except Exception:
        return pd.NaT


def clean_numeric_series(series: pd.Series, remove_text: str | None = None) -> pd.Series:
    """
    Clean a numeric-like pandas Series:
    - optional text removal (e.g. 'EUR')
    - replace comma by dot
    - trim spaces
    - convert to numeric
    """
    cleaned = series.astype(str)

    if remove_text:
        cleaned = cleaned.str.replace(remove_text, "", regex=False)

    cleaned = cleaned.str.replace(",", ".", regex=False).str.strip()
    return pd.to_numeric(cleaned, errors="coerce")


def standardize_text_series(series: pd.Series, case: str | None = None) -> pd.Series:
    """
    Standardize text values while preserving missing values.
    case:
    - 'upper'
    - 'lower'
    - 'title'
    - None
    """
    cleaned = series.str.strip()

    if case == "upper":
        cleaned = cleaned.str.upper()
    elif case == "lower":
        cleaned = cleaned.str.lower()
    elif case == "title":
        cleaned = cleaned.str.title()

    return cleaned


def log_missing_values(logger: logging.Logger, df: pd.DataFrame, title: str) -> None:
    """
    Log the number of missing values per column.
    """
    logger.info("=== %s ===", title)
    logger.info("\n%s", df.isna().sum())


def save_dataframe(df: pd.DataFrame, file_path: str, logger: logging.Logger | None = None) -> None:
    """
    Save a DataFrame to CSV and optionally log the export.
    """
    df.to_csv(file_path, index=False)
    if logger is not None:
        logger.info("File saved successfully: %s", file_path)


def write_text_file(file_path: str, content: str, logger: logging.Logger | None = None) -> None:
    """
    Write plain text content to a file and optionally log the export.
    """
    Path(file_path).write_text(content, encoding="utf-8")
    if logger is not None:
        logger.info("Text file created successfully: %s", file_path)
