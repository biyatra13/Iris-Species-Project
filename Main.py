""""This is main file to run the web app"""

# import necessary modules
import streamlit as st

# import pages
import Home, Data, Prediction, Visualization, Model, About

# Dictionary for pages
pages = {
    "Home": Home,
    "Data Info": Data,
    "Prediction": Prediction,
    "Visualization": Visualization,
    "Model info": Model,
    "About me": About
}

# Creating sidebar navigation
st.sidebar.title("Navigation")
# get value of selected page using radio
page = st.sidebar.radio("Pages", list(pages.keys()))

# Call app funciton for the selected page
pages[page].app()