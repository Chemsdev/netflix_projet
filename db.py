import mysql.connector

# Paramètre de connexion.
import pymysql
from dotenv import load_dotenv
import os
import streamlit as st 
from tools import *

# ======================================================================================>

# Fonction permettent d'insérer les données.
def insert_data_to_database(data, table1, table2, columns_features, connexion):
    
    # Insertion table 1.
    cursor = connexion.cursor()
    value_features = list(data.values())
    del value_features[-1]
    table1_sql = f"INSERT INTO {table1} ({', '.join(columns_features)}) VALUES ({', '.join(['%s' for _ in range(len(columns_features))])})"
    cursor.execute(table1_sql, value_features)


    # Insertion table 2.
    inserted_id = cursor.lastrowid
    table2_columns = ["id_fk", "y_pred"]
    table2_values = [inserted_id, data["Prediction"]]
    table2_sql = f"INSERT INTO {table2} ({', '.join(table2_columns)}) VALUES ({', '.join(['%s' for _ in range(len(table2_columns))])})"
    cursor.execute(table2_sql, table2_values)

    print("Données insérées avec succès.")
    connexion.commit()

# ======================================================================================>

# Fonction
def send_db(data):
    
    # connexion à la db.
    cnx = connect()
    cursor = cnx.cursor()    

    # Insertion des données.
    insert_data_to_database(
        data=data,
        table1="personne",
        table2="film",
        columns_features=["A", "B", "C", "D", "E"],
        connexion=cnx
    )

    # Fermeture connexion.
    cursor.close()
    
