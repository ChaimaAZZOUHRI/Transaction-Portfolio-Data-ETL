from utils import setup_logger
import pandas as pd


logger = setup_logger("exploration.log", __name__)


def main() -> None:
    df = pd.read_csv("bank_transactions.csv")

    logger.info("=== DATASET OVERVIEW ===")
    logger.info("\n%s", df.head())

    logger.info("=== SHAPE ===")
    logger.info("%s", df.shape)

    logger.info("=== COLUMN NAMES ===")
    logger.info("%s", df.columns.tolist())

    logger.info("=== DATA TYPES ===")
    logger.info("\n%s", df.dtypes)

    logger.info("=== DESCRIPTIVE STATISTICS ===")
    logger.info("\n%s", df.describe(include="all").transpose())

    logger.info("=== MISSING VALUES COUNT ===")
    logger.info("\n%s", df.isna().sum())

    logger.info("=== MISSING VALUES PERCENTAGE ===")
    logger.info("\n%s", (df.isna().mean() * 100).round(2).sort_values(ascending=False))

    logger.info("=== DUPLICATES BASED ON transaction_id ===")
    logger.info("%s", df.duplicated(subset=["transaction_id"]).sum())

    duplicate_rows = df[df.duplicated(subset=["transaction_id"], keep=False)].sort_values("transaction_id")
    logger.info("=== DUPLICATE ROWS PREVIEW ===")
    logger.info("\n%s", duplicate_rows.head(20))

    cols_to_check = ["devise", "segment_client", "type_operation", "statut", "agence"]
    for col in cols_to_check:
        if col in df.columns:
            logger.info("=== UNIQUE VALUES IN %s ===", col)
            logger.info("%s", df[col].dropna().astype(str).unique())

    logger.info("Exploration step completed successfully.")


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError:
        logger.error("The file 'bank_transactions.csv' was not found.")
        raise
    except KeyError as e:
        logger.error("The column %s is missing from the dataset.", e)
        raise
    except Exception as e:
        logger.exception("An unexpected error occurred: %s", e)
        raise
