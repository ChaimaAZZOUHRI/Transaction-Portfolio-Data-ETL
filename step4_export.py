import pandas as pd

from utils import setup_logger, write_text_file


logger = setup_logger("export.log", __name__)


def main() -> None:
    df = pd.read_csv("financecore_step2_enriched.csv")
    logger.info("Enriched file loaded successfully.")

    logger.info("=== FINAL SHAPE ===")
    logger.info("%s", df.shape)

    logger.info("=== FINAL DATA TYPES ===")
    logger.info("\n%s", df.dtypes)

    logger.info("=== FINAL MISSING VALUES ===")
    logger.info("\n%s", df.isna().sum())

    critical_cols = [
        "transaction_id", "client_id", "date_transaction", "montant",
        "devise", "agence", "type_operation", "statut",
        "score_credit_client", "segment_client"
    ]
    missing_critical = df[critical_cols].isna().sum()
    logger.info("=== FINAL MISSING VALUES IN CRITICAL COLUMNS ===")
    logger.info("\n%s", missing_critical)

    df.to_csv("financecore_clean.csv", index=False)
    logger.info("Final cleaned file exported: financecore_clean.csv")

    decisions_text = """# DECISIONS.md

## Cleaning decisions for FinanceCore SA dataset

1. Removed duplicates based on `transaction_id` using `keep="first"`.
2. Standardized `date_transaction` into the format `YYYY-MM-DD HH:MM:SS`.
3. Cleaned `montant` by replacing commas with dots and converting values to float.
4. Cleaned `solde_avant` by removing the `EUR` suffix and converting values to float.
5. Normalized `devise` to uppercase.
6. Harmonized `segment_client` using title case.
7. Removed extra spaces from `agence`.
8. Imputed missing values:
   - `score_credit_client` with median
   - `segment_client` with mode
   - `agence` with mode
9. Dropped `taux_interet` because it was 100% missing.
10. Detected anomalies using:
   - IQR on `montant`
   - business rules on suspicious amounts
   - invalid credit score rules
11. Kept anomalies and flagged them with `is_anomaly`.
12. Added engineered features:
   - `annee`, `mois`, `trimestre`, `jour_semaine`
   - `montant_eur_verifie`
   - `ecart_montant_eur`
   - `categorie_risque`
   - `solde_net_client`
   - `nb_transactions`
   - `montant_moyen`
   - `nb_produits_distincts`
   - `taux_rejet_agence`
"""
    write_text_file("DECISIONS.md", decisions_text, logger)


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError:
        logger.error("The file 'financecore_step2_enriched.csv' was not found.")
        raise
    except Exception as e:
        logger.exception("An unexpected error occurred: %s", e)
        raise
