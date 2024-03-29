import streamlit as st

# Import Our Mini Apps
from eda_app import run_eda_app 
from ml_app import run_ml_app

st.title("Main App")

menu = ["Home", "EDA", "ML", "About"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Home")

elif choice == "EDA":
    run_eda_app()

elif choice == "ML":
    run_ml_app()

else:
    st.subheader("About")
