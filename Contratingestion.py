from connection import get_connection
import csv
import os
#ingest data from CSV file into PostgreSQL

from datetime import datetime


def ingest_data():
    # Connect to PostgreSQL
    conn = get_connection()
    cur = conn.cursor()

    # Open the CSV file
    csv_path = os.path.join(os.path.dirname(__file__), 'DATA', 'Contrat.csv')
    with open(csv_path, 'r', encoding='cp1252') as file:  # 👈 fix encoding
        data_reader = csv.reader(file, delimiter=';')      # 👈 fix delimiter
        next(data_reader)  # Skip header row

        sql = """
        INSERT INTO contrats (
            ref_personne, num_contrat, lib_produit, effet_contrat,
            date_expiration, prochain_terme, lib_etat_contrat,
            branche, somme_quittances, statut_paiement, capital_assure
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        numeric_cols = [8, 10]  # somme_quittances, capital_assure
        date_cols = [3, 4, 5]   # effet_contrat, date_expiration, prochain_terme

        for row in data_reader:
            cleaned_row = []
            for i, val in enumerate(row):
                val = val.strip()

                # Treat NULL, empty, or invalid numbers as None
                if val.upper() in ["NULL", "#N/A", "NA"] or val == "":
                    cleaned_row.append(None)
                else:
                    # Convert numeric columns
                    if i in numeric_cols:
                        try:
                            val = float(val.replace(",", "."))
                        except ValueError:
                            val = None
                        cleaned_row.append(val)
                    # Convert date columns
                    elif i in date_cols:
                        try:
                            date_obj = datetime.strptime(val[:10], "%Y-%m-%d")
                            cleaned_row.append(date_obj)
                        except ValueError:
                            cleaned_row.append(None)
                    else:
                        cleaned_row.append(val)

            cur.execute(sql, cleaned_row)

    # Commit and close the connection
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Data ingested successfully")



if __name__ == "__main__":
    ingest_data()