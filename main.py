import pandas as pd
import streamlit as st 
from model import *
from tools import *

def main():

    # background + titre
    background_front(url="https://wallpapers.com/images/hd/netflix-background-ay2odaz7o4zltn0q.jpg")
    st.title("Recommandation Films")
    
    # Récupération des titres des films 
    title_movies = get_title_movies()
    
    # Le formulaire.
    with st.form("my_form"):
        
        # Dictionnaire contenant l'input de choix du film.
        movie = st.selectbox('Veuillez choisir un film...', (title_movies))
        
        # Bouton d'envoi du formulaire.
        submitted = st.form_submit_button("Envoyer")
        
        # Si l'utilisateur clique sur envoyer :
        if submitted:
            
            # Execution du model et affichage du résultat.
            top_recommendations = get_top_recommendations(movie_title=movie)
            
            # Ajout de la prédiction et du film choisis.
            data={}
            data["movie"] = movie
            
            # Nettoyage des prédictions.
            predictions = [i.replace(" ", "").replace("\xa0", "") for i in top_recommendations["movie_title"]]
            data["predictions"] = predictions
            
            # Insertion des données.
            insert_data_to_database(data=data)

main()

