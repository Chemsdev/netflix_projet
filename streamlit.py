import pandas as pd
import streamlit as st 


def main():
    st.write("Hello")

    with st.form("my_form"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")

        submitted = st.form_submit_button("Envoyer")
        if submitted:
            st.write("Les prédictions :")


main()