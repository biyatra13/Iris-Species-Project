"""This is the prediction page of the web app"""

# Import necessary modules
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.svm import SVC

# Import our modules
from Preprocess import load_data, load_model


def app():
    """This funciton runs the prediction page"""

    # Set the title of the page
    st.title("Welcome to the prediction page")

    # Get features and target from the dataset
    X, y = load_data()
    des = X.describe()

    target_dict = {
        0: "Iris-virginica",
        1: "Iris-versicolor",
        2: "Iris-setosa"
    }

    f1_min = float(des["SepalLengthCm"]['min'])
    f1_max = float(des["SepalLengthCm"]['max'])

    f2_min = float(des["SepalWidthCm"]['min'])
    f2_max = float(des["SepalWidthCm"]['max'])

    f3_min = float(des["PetalLengthCm"]['min'])
    f3_max = float(des["PetalLengthCm"]['max'])

    f4_min = float(des["PetalWidthCm"]['min'])
    f4_max = float(des["PetalWidthCm"]['max'])

    # Take input of features from the user.
    f1 = st.slider("Sepal Length(Cm)", f1_min, f1_max)
    f2 = st.slider("Sepal Width(Cm)", f2_min, f2_max)
    f3 = st.slider("Petal Length(Cm)", f3_min, f3_max)
    f4 = st.slider("Petal Width(Cm)", f4_min, f4_max)


    # Create user input features list
    feat_list = pd.DataFrame([[f1, f2, f3, f4]])

    # Get model and score
    model, score = load_model(SVC)

    # Create a button to get the prediction values on click
    if (st.button("Predict")):
        # Predict the values and show it to the user
        pred = model.predict(feat_list)
        pred = pred[0]
        pred_value = target_dict[pred]
        st.success("Prediction Sucessful!!!")
        st.warning(f"Predicted specie {pred_value}")
        st.info(f"Accuracy is {round(score * 100, 2)}")

