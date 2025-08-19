# From Excel To PostgreSQL using CSV

## Instructions

1. Download `requirements.txt`.
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
MORE INFOs :  
[Ressource 1 (article)](https://hevodata.com/learn/excel-to-postgresql/) <br>
[Ressource 2 (video)](https://www.youtube.com/watch?v=ijVfaCq21oU&ab_channel=IOTStation)

# PGAdmin Configuration : 
## 1. Excel → CSV

Simply save your Excel file as a CSV file.  

## 1.5 Configure the Database : 
after connecting to PGadmin : Databases> Create> database
Open Query tool (right click on the newly created DB > query tool) 

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
```
### Personnes Physique Table :

```sql
CREATE TABLE personnesPhy (
    ref_personne          VARCHAR(20),
    nom_prenom            TEXT,
    date_naissance        DATE,
    lieu_naissance        TEXT,
    code_sexe             CHAR(1),
    situation_familiale   TEXT,
    num_piece_identite    VARCHAR(20),
    lib_secteur_activite  TEXT,
    lib_profession        TEXT,
    ville                 TEXT,
    lib_gouvernorat       TEXT,
    ville_gouvernorat     TEXT
);
```
### Personnes Morale Table : 
```sql
CREATE TABLE societes (
    ref_personne        VARCHAR(20),
    raison_sociale      TEXT,
    matricule_fiscale   VARCHAR(20),
    lib_secteur_activite TEXT,
    lib_activite        TEXT,
    ville               TEXT,
    lib_gouvernorat     TEXT,
    ville_gouvernorat   TEXT
);
```
### Sinistre Table: 
````sql
CREATE TABLE sinistres (
    num_sinistre           VARCHAR(20),
    num_contrat            VARCHAR(20),
    lib_branche            TEXT,
    lib_sous_branche       TEXT,
    lib_produit            TEXT,
    nature_sinistre        TEXT,
    lib_type_sinistre      TEXT,
    taux_responsabilite    NUMERIC(5,2),
    date_survenance        DATE,
    date_declaration       DATE,
    date_ouverture         DATE,
    observation_sinistre   TEXT,
    lib_etat_sinistre      TEXT,
    lieu_accident          TEXT,
    motif_reouverture      TEXT,
    montant_encaisse       NUMERIC(12,2),
    montant_a_encaisser    NUMERIC(12,2)
);
````
### Mapping Produit Table : 
````sql
CREATE TABLE mappingproduits (
    lib_branche       TEXT,
    lib_sous_branche  TEXT,
    lib_produit       TEXT
);
````

# RUN YOUR CODE : ) 
