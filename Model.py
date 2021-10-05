"""This page is for model info"""

# Import necessary modules
import streamlit as st


def app():
    """This function runs the model info page"""
    # Add title to page
    st.title("Welcome to the model info page")

    # Add image
    st.image("./Iris Img1.jpg", width=500)

    # Add model description
    st.write("model description")