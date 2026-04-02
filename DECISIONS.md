# DECISIONS.md

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
