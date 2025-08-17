from connection import get_connection
import csv
import os

def ingest_data():
    # Connect to PostgreSQL
    conn = get_connection()
    cur = conn.cursor()

    # CSV file path
    csv_path = os.path.join(os.path.dirname(__file__), 'DATA', 'PersonMorale.csv')
    with open(csv_path, 'r', encoding='latin1') as file:  # handle Excel encoding
        data_reader = csv.reader(file, delimiter=';')       # handle semicolon delimiter
        next(data_reader)  # skip header

        sql = """
        INSERT INTO personnesMor (
            ref_personne, raison_sociale, matricule_fiscale, lib_secteur_activite,
            lib_activite, ville, lib_gouvernorat, ville_gouvernorat
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        for row in data_reader:
            cleaned_row = []
            for val in row:
                val = val.strip()
                if val.upper() in ["NULL", "#N/A", "NA"] or val == "":
                    cleaned_row.append(None)
                else:
                    cleaned_row.append(val)

            cur.execute(sql, cleaned_row)

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Societes data ingested successfully")


if __name__ == "__main__":
    ingest_data()
