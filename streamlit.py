import pandas as pd
import streamlit as st 
from db import *

def main():
    st.write("Hello")

    with st.form("my_form"):
        st.write("Veuillez remplir le formulaire")
        
        dictionnaire = {
            "input1" : st.text_input("Champ 1"),
            "input2" : st.text_input("Champ 2"),
            "input3" : st.text_input("Champ 3"),
            "input4" : st.text_input("Champ 4")    
        }

        submitted = st.form_submit_button("Envoyer")
        if submitted:
            
            # envoyer les données.
            send_db(dict=dictionnaire)
            
            # Affichage des résultats.
            st.write("Les prédictions :")



main()