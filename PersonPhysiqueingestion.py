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
    csv_path = os.path.join(os.path.dirname(__file__), 'DATA', 'PersonPhysique.csv')
    with open(csv_path, 'r', encoding='latin1') as file:  # 👈 fix encoding
        data_reader = csv.reader(file, delimiter=';')      # 👈 fix delimiter
        next(data_reader)  # Skip header row


        sql = """
            INSERT INTO personnesPhy (
                ref_personne, nom_prenom, date_naissance, lieu_naissance,
                code_sexe, situation_familiale, num_piece_identite,
                lib_secteur_activite, lib_profession, ville,
                lib_gouvernorat, ville_gouvernorat
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        for row in data_reader:
            cleaned_row = []
            for i, val in enumerate(row):
                val = val.strip()

                # Treat NULL, empty, or placeholders as None
                if val.upper() in ["NULL", "#N/A", "NA"] or val == "":
                    cleaned_row.append(None)
                # Convert date columns
                
                else:
                    cleaned_row.append(val)

            cur.execute(sql, cleaned_row)

    # Commit and close the connection
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Personnes data ingested successfully")


if __name__ == "__main__":
    ingest_data()