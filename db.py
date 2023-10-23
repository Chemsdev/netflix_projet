import mysql.connector

# Paramètre de connexion.
import pymysql
from dotenv import load_dotenv
import os


# Initialisation connexion BDD.
def connect():
    load_dotenv('.env')
    cnx = pymysql.connect(
        user     = "chemsdine",
        password = os.getenv("DB_PASSWORD"),
        host     = "chemsdineserver.mysql.database.azure.com",
        database = "netflix",
        ssl      = {'ssl_disabled': os.getenv("DB_SSL_DISABLED") == "True"}
    )
    return cnx

# cnx = connect()
# cursor = cnx.cursor()    

# Fonction permettant de créer les tables dans une base de données.
def create_tables(table_name_1: str, table_name_2: str, connexion, cursor):
    # Table 1.
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name_1}
        (id INT AUTO_INCREMENT PRIMARY KEY,
         A INTEGER,
         B INTEGER,
         C TEXT,
         D INTEGER,
         E TEXT
        )''')
    print(f"Table '{table_name_1}' créée avec succès.")

    # Table 2.
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name_2}
        (id INT AUTO_INCREMENT PRIMARY KEY,
         id_fk INT,
         y_pred TEXT,
         FOREIGN KEY (id_fk) REFERENCES {table_name_1}(id)
        )''')
    print(f"Table '{table_name_2}' créée avec succès.")
    connexion.commit()


cnx = connect()
cursor = cnx.cursor()    
create_tables(table_name_1="A", 
              table_name_2="B", 
              connexion=cnx, 
              cursor=cursor
)
cursor.close()