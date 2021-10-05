"""This is about page"""

# import necessary modules
import streamlit as st


def app():
    """This function runs the about page"""
    # Add balloons animation when page opens
    st.balloons()

    # Add title
    st.title("Welcome to the About Me page")

    # Add an image
    #st.image("./images/iris_classification_model.jpg")

    # Add Contact Details
    st.header('Contact Us')

    # Add email
    st.markdown('''### Name:
    Biyatra Ghosh''')

    # Add name
    st.markdown('''### Email:
    biyatraghosh13@gmail.com''')

    # Add github
    st.markdown('''### GitHub: [Biyatra Ghosh](https://github.com/biyatra13)''')

    # Add linkedin
    st.markdown('''### Linkedin: [Biyatra Ghosh](https://www.linkedin.com/in/biyatra-ghosh-b14128208/)''')