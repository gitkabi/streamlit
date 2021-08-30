import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.title("Plotting In Streamlit with Plotly")
df = pd.read_csv("/home/kabigaruda/streamlit/reli.csv")
st.dataframe(df)

fig = px.pie(df, values= 'Open', names = 'Close', title= 'Pie Chart of Reliance Stocks')
st.plotly_chart(fig)

fig2 = px.bar(df,x = 'Open', y = 'Close')
st.plotly_chart(fig2)  