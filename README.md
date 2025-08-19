# From Excel To PostgreSQL using CSV

## Instructions

1. Download `requirements.txt`.
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
MORE INFOs :  
[Ressource 1 (article)](https://hevodata.com/learn/excel-to-postgresql/) <br>
[Ressource 2 (video)](https://www.youtube.com/watch?v=ijVfaCq21oU&ab_channel=IOTStation)

##PGAdmin Configuration : 
## 1. Excel → CSV

Simply save your Excel file as a CSV file.  

**Example:**  

![Excel Example 1](attachment:bc6f3e06-d064-4fbd-b9e3-cb1de4881f09:image.png)  
![Excel Example 2](attachment:10727a3c-eeaa-447d-a415-9e5a29470fab:image.png)

---

## 2. Create Tables

We will create PostgreSQL tables based on the column names of each CSV file.

### Contract Table

```sql
CREATE TABLE contrats (
    ref_personne      VARCHAR(50),
    num_contrat       VARCHAR(50) PRIMARY KEY,
    lib_produit       TEXT,
    effet_contrat     DATE,
    date_expiration   DATE,
    prochain_terme    DATE,
    lib_etat_contrat  TEXT,
    branche           TEXT,
    somme_quittances  NUMERIC(12,2),
    statut_paiement   TEXT,
    capital_assure    NUMERIC(12,2)
);
