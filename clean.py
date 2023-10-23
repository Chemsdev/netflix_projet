import pandas as pd
from tools import *
from sqlalchemy import create_engine


# Envoie raw data.
def send_raw_data():
    raw_netflix = pd.read_csv("movie_metadata.csv")
    engine = create_engine('mysql://root:@5.tcp.eu.ngrok.io:14544/netflix')
    conn = engine.connect()
    raw_netflix.to_sql(name='netflix_raw', con=conn, if_exists='append')
    engine.close()
    print("raw data envoyé avec succès !")
  
# Envoie data nettoyée.  
def send_clean_data():
    engine = create_engine('mysql://root:@5.tcp.eu.ngrok.io:14544/netflix')
    conn = engine.connect()
    conn.execute("SELECT * FROM netflix_raw")
    engine.close()
    
    # nettoyage
    clean_netflix = 2
    clean_netflix.to_sql(name='clean_netflix', con=conn, if_exists='append')
    print("data nettoyée envoyé avec succès !")
    
    
send_raw_data()

