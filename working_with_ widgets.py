from numpy import character
import streamlit as st

# Working with wigets
# Buttons/Radio/Checkbox/Select/

# Working with Buttons

note = "Sucecssfully sumbitted"

if st.button("Submit"):
    st.write("Note: {}".format(note.upper()))

if st.button("Submit",key='new02'): # (key='new02') is used to avoid duplicate
    st.write("Note: {}".format(note.lower()))

if st.button("Submit",key='new03'): # (key='new02') is used to avoid duplicate
    st.write("Note: {}".format(note.upper()))

#Working with radio buttons

status = st.radio("What is your status",("Active","Inactive")) # It will promt for Active or inactive

if status == 'Active':
    st.success("You are active")
elif status == 'Inactive':
    st.warning("You are inactive") 

# Working with Checkbox

if st.checkbox("Show/Hide"):
    st.title("Welcome to streamlit") 

# Working with Expander

if st.expander("Python"): # 1st way 
    st.info("Hello Python")

with st.expander("Kabi"): # 2nd way
    st.error("Hello Kabi") # (with statement puts context inside the box)