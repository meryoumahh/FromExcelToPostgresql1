from connection import get_connection
import csv
import os

def ingest_data():
    conn = get_connection()
    cur = conn.cursor()

    csv_path = os.path.join(os.path.dirname(__file__), 'DATA', 'MappingProduit.csv')
    with open(csv_path, 'r', encoding='latin1') as file:  # 👈 handle accented characters
        data_reader = csv.reader(file, delimiter=';')
        next(data_reader)  # skip header row

        sql = """
        INSERT INTO MappingProduits (lib_branche, lib_sous_branche, lib_produit)
        VALUES (%s, %s, %s)
        """

        for row in data_reader:
            cleaned_row = [val.strip() if val.strip().upper() != "NULL" else None for val in row]
            cur.execute(sql, cleaned_row)

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Produits data ingested successfully")


if __name__ == "__main__":
    ingest_data()
