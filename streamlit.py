import pandas as pd
import streamlit as st 


def main():
    st.write("Hello")

    with st.form("my_form"):
        st.write("Veuillez remplir le formulaire")
        input1 = st.text_input("Champ 1")
        input2 = st.text_input("Champ 2")
        input3 = st.text_input("Champ 3")
        input4 = st.text_input("Champ 4")    
        submitted = st.form_submit_button("Envoyer")
        if submitted:
            st.write("Les prédictions :")
            # Ajoutez ici le code pour traiter les prédictions en fonction des valeurs des champs.



main()