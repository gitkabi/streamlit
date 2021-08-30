from pandas.core.frame import DataFrame
import streamlit as st

import pandas as pd
import numpy as np
import altair as alt

st.title("Plotting In Streamlit")

# Load Dataset
df = pd.read_csv("/home/kabigaruda/streamlit/reli.csv")
df2 = pd.read_csv("/home/kabigaruda/streamlit/Leaves.csv")
st.dataframe(df2.head())

# Bar Chart
# Using st.bar_chart
#st.bar_chart(df[["High", "Open", "Close"]]) 

# Line chart
lang_list = df2.columns.tolist()
lang_choices = st.multiselect("Choose Language",lang_list)
new_df = df2[lang_choices]
st.line_chart(new_df)

# Area Chart
st.area_chart(new_df, use_container_width= True)

# Altair
df2 = pd.DataFrame(
np.random.randn(200, 3),
columns= ['a', 'b' ,'c'])
c = alt.Chart(df2).mark_circle().encode(
 x = 'a' , y = 'b' , size = 'c', color = 'c', tooltip = ['a', 'b', 'c'])
st.dataframe(df2.head()) 

# Method 1 (Usig Write)
st.write(c)
    
# Method 2 (Using st.altair_chart)
st.altair_chart(c, use_container_width= True)