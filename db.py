import mysql.connector

# Paramètre de connexion.
import pymysql
from dotenv import load_dotenv
import os


# Initialisation connexion BDD.
def connect():
    load_dotenv('.env')
    cnx = pymysql.connect(
        user     = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        host     = os.getenv("DB_HOST"),
        port     = int(os.getenv("DB_PORT")),
        database = os.getenv("DB_NAME"),
        ssl      = {'ssl_disabled': os.getenv("DB_SSL_DISABLED") == "True"}
    )
    return cnx


# Fonction permettant de créer les tables dans une base de données.
def create_tables(table_name_1: str, table_name_2: str, connexion=cnx, cursor=cursor):
    
    # Table 1.
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name_1}
        (id INT AUTO_INCREMENT PRIMARY KEY,
         INTEGER,
         INTEGER,
         INTEGER,
         TEXT,
         TEXT,
         TEXT,
        ''')
    print(f"Table '{table_name_1}' créée avec succès.")    
    
    # Table 2.
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name_2}
                (id INT AUTO_INCREMENT PRIMARY KEY,
                id_fk INT,
                y_pred TEXT,
                FOREIGN KEY (id_fk) REFERENCES {table_name_1}(id))''')
    print(f"Table '{table_name_2}' créée avec succès.")
    connexion.commit()
    
    