from connection import get_connection
import csv
import os
from datetime import datetime

def ingest_data():
    conn = get_connection()
    cur = conn.cursor()

    csv_path = os.path.join(os.path.dirname(__file__), 'DATA', 'Sinistre.csv')
    with open(csv_path, 'r', encoding='latin1') as file:
        data_reader = csv.reader(file, delimiter=';')
        next(data_reader)  # skip header

        sql = """
        INSERT INTO sinistres (
            num_sinistre, num_contrat, lib_branche, lib_sous_branche,
            lib_produit, nature_sinistre, lib_type_sinistre, taux_responsabilite,
            date_survenance, date_declaration, date_ouverture,
            observation_sinistre, lib_etat_sinistre, lieu_accident,
            motif_reouverture, montant_encaisse, montant_a_encaisser
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        numeric_cols = [7, 15, 16]  # indices of numeric columns
        date_cols = [8, 9, 10]      # indices of date columns

        for row in data_reader:
            cleaned_row = []
            for i, val in enumerate(row):
                val = val.strip()

                if val.upper() in ["NULL", "#N/A", "NA"] or val == "":
                    cleaned_row.append(None)
                elif i in numeric_cols:
                    try:
                        cleaned_row.append(float(val.replace(",", ".")))
                    except ValueError:
                        cleaned_row.append(None)
                elif i in date_cols:
                    try:
                        date_obj = datetime.strptime(val[:10], "%Y-%m-%d")
                        cleaned_row.append(date_obj)
                    except ValueError:
                        cleaned_row.append(None)
                else:
                    cleaned_row.append(val)

            cur.execute(sql, cleaned_row)

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Sinistres data ingested successfully")


if __name__ == "__main__":
    ingest_data()
