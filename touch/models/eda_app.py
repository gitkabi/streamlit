import streamlit as st

# Load EDA Pkgs
import pandas as pd

def run_eda_app():
    st.subheader("From Exploratory Data Analysis")
    df = pd.read_csv("/home/kabigaruda/streamlit/touch/data/reli.csv")
    st.dataframe(df)
