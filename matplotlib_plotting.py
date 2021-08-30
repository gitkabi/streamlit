import streamlit as st

# Load EDA Packages
import pandas as pd
import numpy as np

# Load Data Viz. Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns


st.title("Plotting with st.pyplot")
df = pd.read_csv("/home/kabigaruda/streamlit/reli.csv")

st.dataframe(df.head())

# Newest method
fig, ax = plt.subplots()   # }
ax.bar([1,2,3], [1,2,3])   # } (New way to plot using pyplot)  
st.pyplot(fig)             # } ( Bar Method)

fig, ax = plt.subplots()       # }
ax.scatter([1,2,3], [1,2,3])   # } (Scatter Method)  
st.pyplot(fig)                 # }

# Method 2: simple Method
penguins = sns.load_dataset("penguins")
st.title("Hello")
fig = sns.pairplot(penguins, hue="species")
st.pyplot(fig)
