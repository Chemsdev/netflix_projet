# Paramètre de connexion.
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Initialisation connexion BDD.
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pymysql


# ================================================================================>

# Fonction permettant de se connecter à la base de données.
def connect():
    load_dotenv('.env')
    engine = create_engine('mysql+pymysql://root:@5.tcp.eu.ngrok.io:14544/netflix')
    conn = engine.connect()
    return conn

# ================================================================================>

# Fonction permettant de créer les tables dans une base de données.
def create_tables(table_name_1: str, table_name_2: str, table_name_3: str):
    # Connexion à la base de données
    conn = connect()

    # Création d'un objet cursor pour exécuter des requêtes SQL
    cursor = conn.connection.cursor()

    # Table 1.
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name_1}
        (id_name INT AUTO_INCREMENT PRIMARY KEY,
        Name TEXT,
        nb_like INTEGER
        )''')
    print(f"Table '{table_name_1}' créée avec succès.")

    # Table 2.
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name_2}
        (id_movie INT AUTO_INCREMENT PRIMARY KEY,
        id_name_fk INT,
        title TEXT,
        plot TEXT,
        ratio INTEGER,
        FOREIGN KEY (id_name_fk) REFERENCES {table_name_1}(id_name)
        )''')
    print(f"Table '{table_name_2}' créée avec succès.")

    # Table 3.
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name_3}
        (id_prediction INT AUTO_INCREMENT PRIMARY KEY,
        id_movie_fk INT,
        prediction_result TEXT,
        FOREIGN KEY (id_movie_fk) REFERENCES {table_name_2}(id_movie)
        )''')
    print(f"Table '{table_name_3}' créée avec succès.")

    # Valider les modifications dans la base de données
    conn.connection.commit()

    # Fermer la connexion
    conn.close()


# ======================================================================================>



create_tables(
    table_name_1="Popularity", 
    table_name_2="Movies", 
    table_name_3="Predictions"
)