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
        dictionnaire = {
            "input1" : st.text_input("Champ 1"),
            "input2" : st.text_input("Champ 2"),
            "input3" : st.text_input("Champ 3"),
            "input4" : st.text_input("Champ 4")    
        }
        
        # Envoi du formuaire.
        submitted = st.form_submit_button("Envoyer")
        if submitted:
            
            # envoyer les données.
            send_db(dict=dictionnaire)
            
            # Affichage des résultats.
            st.write("Les prédictions :")



main()