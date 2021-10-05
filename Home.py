import  streamlit as st


def  app():
    """This function runs the home page"""
    # Add title to the home page
    st.title("Welcome to the home page")
    # Add image to the home page
    st.image("./Iris Img1.jpg",width=500)
    # Add brief describtion of your web app
    st.text("This web app helps in the prediction of Iris Specie using SVM Model.")