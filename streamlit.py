import pandas as pd
import streamlit as st 
from db import *
from front import *

def main():

    
    background_front(url="https://wallpapers.com/images/hd/netflix-background-ay2odaz7o4zltn0q.jpg")
    st.title("Recommandation Films")
    
    # Le formulaire.
    with st.form("my_form"):
        st.write("Veuillez remplir le formulaire")
        
        # Dictionnaire contenant les inputs.
        data = {
            "input1" : st.text_input("Champ 1"),
            "input2" : st.text_input("Champ 2"),
            "input3" : st.text_input("Champ 3"),
            "input4" : st.text_input("Champ 4"),
            "input5" : st.text_input("Champ 5")  
        }
    
        # Ajout de la prédiction.
        data["Prediction"] = "coucou"
        
        # Envoi du formuaire.
        submitted = st.form_submit_button("Envoyer")
        if submitted:
            
            # envoyer les données.
            send_db(data=data)
            
            # Affichage des résultats.
            st.write("Les prédictions :")


main()