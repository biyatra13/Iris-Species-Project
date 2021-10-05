"""This page is data page"""

# Import necessary
import streamlit as st
import pandas as pd

# Import function
from Preprocess import load_data


def app():
    """This function runs the data info page"""
    # Add title to the page
    st.title("Welcome to the Data Info page")

    # Add subheader for the section
    st.subheader("View Data")

    # Load the dataset
    X, y = load_data()
    df = pd.concat([X, y], axis=1)

    # Create an expansion option to check the data
    with st.expander("View data"):
        st.dataframe(df)

    # Create a section to columns values
    # Give subheader
    st.subheader("Columns Summary:")

    # Create a checkbox to get the summary.
    if st.checkbox("View Summary"):
        st.dataframe(df.describe())

    # Create multiple check box in row
    col_name, col_dtype, col_data = st.columns(3)

    # Show name of all dataframe
    with col_name:
        if st.checkbox("Column Names"):
            st.dataframe(df.columns)

    # Show datatype of all columns
    with col_dtype:
        if st.checkbox("Columns data types"):
            dtypes = df.dtypes.apply(lambda x: x.name)
            st.dataframe(dtypes)

    # Show data for each columns
    with col_data:
        if st.checkbox("Columns Data"):
            col = st.selectbox("Column Name", list(df.columns))
            st.dataframe(df[col])

