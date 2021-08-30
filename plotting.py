import streamlit as st

#Load EDA Pkg
import pandas as pd
import numpy as np

#Load Data Vis Pkg
import plotly.express as px

st.title("Plotting n Streamlit with Plotly")
df = pd.read_csv("/home/kabigaruda/streamlit/Leaves.csv")
st.dataframe(df)

fig = px.pie(df,values= 'Unnamed: 0', names = 'Unnamed: 3', title = 'Pie Chart Of Language')
st.plotly_chart(fig)

fig2 = px.bar(df, x='Unnamed: 0', y='Unnamed: 3')
st.plotly_chart(fig2)