import streamlit as st
import pandas as pd

# Display data
df = pd.read_csv("reli.csv")

# Method 1
st.dataframe(df,1000,1000) # (Value indicates the size)

# Method 2
st.table(df)

# Adding a color style from pandas
st.dataframe(df.style.highlight_max(axis=0, color= "red"))

st.table(df.style.highlight_max(axis=0, color= "green")) 

# Method 3: Using superfunction st.write
st.write(df.head())

# Dislay json
st.json({'data' : 'name'})# (To display json format)

# Display code
mycode = """
def sayhello():
    print("Hello Streamlit Lovers)
"""
st.code(mycode,language= 'python') # (To define code of ny language)

