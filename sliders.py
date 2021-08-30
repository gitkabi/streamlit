import streamlit as st

# Select/Multiple select
my_lang = ["Python", "ML", "Go"]

choice = st.selectbox("Language", my_lang)
st.warning("You selected {}".format(choice)) # (It displays what you selected)

# Multiple selection

spoken_language = ("English", "Hindi", "Gujarati", "Bengali")
my_spoken_language = st.multiselect("Spoken Language", spoken_language )

spoken_language = ("English", "Hindi", "Gujarati", "Bengali")
my_spoken_language = st.multiselect("Spoken Language", spoken_language,default= "Hindi")

# Slider
age = st.slider("Age", 1, 100, 26) # (For Numbers like Int/Float/Dates)

# Select Slider
#color = st.select_slider("choose_color", options = ["yellow", "blue", "red", "black"],  value = ("yellow")