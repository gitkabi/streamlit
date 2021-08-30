# Core packages
from os import name
import streamlit as st

# Working with displaying texts
st.title("Hello Streamlit lovers")

st.text("This is my first web application")

st.text("My name is Abhishek kabi")

# Header  
st.header("This is in big fonts")

# Subheader
st.subheader("This is in small fonts")

# Title
st.title("This is a title")

# Markdown
st.markdown("## This is markdown") # (Double # to make the font look big)

# Displaying Colored Text/Bootstraps Alert
st.success("Green means sucessful")
st.warning("Yellow means danger")
st.info(" Blue means information")
st.error("Red means error")
st.exception("This is an exception")

# Superfunction
st.write("## This is a markdown text")
st.write(1+2) 

st.write(dir(st)) # It displays all the st directories 

# Help info 
st.help(range)# It gives us information 