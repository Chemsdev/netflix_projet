import mysql.connector

# Paramètre de connexion.
cnx = mysql.connector.connect(
    user          ="chemsdine", 
    password      ="Ounissi69800", 
    host          ="chemsdineserver.mysql.database.azure.com", 
    port          =3306, 
    database      ="retard_avion", 
    ssl_disabled  =False
)
cursor = cnx.cursor()    

# Fonction permettant de créer les tables dans une base de données.
def create_tables(table_name_1: str, table_name_2: str, connexion=cnx, cursor=cursor):
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
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name_2}
                (id INT AUTO_INCREMENT PRIMARY KEY,
                id_fk INT,
                y_pred TEXT,
                FOREIGN KEY (id_fk) REFERENCES {table_name_1}(id))''')
    print(f"Table '{table_name_2}' créée avec succès.")
    connexion.commit()
    
    