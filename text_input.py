import streamlit as st

# Text input
fname = st.text_input("Enter Firstname", max_chars = 10)

# Text Input Hide Password
streamlit = st.text_input("Enter Password", type = "password")
st.title(fname)

# Text area
message = st.text_area("Enter Message", max_chars = 1000, height = 200)
st.warning(message)

# Numbers
numbers = st.number_input("Enter Number", 1, 50, 5)

# Date input
myappointment =  st.date_input("Appointment") # (it gives a calender on output)

# Time input
mytime = st.time_input("My Time")

# Color Picker
color = st.color_picker("Select color")