# Core packages
import streamlit as st
from PIL import Image
from streamlit import config

img = Image.open("image.jpg")

# Method 1
st.set_page_config(page_title = 'My App',
    page_icon= 'img', layout = 'wide',
    initial_sidebar_state = 'expanded') # (auto and collapsed can also be used)

st.set_page_config(page_title = 'My App',
    page_icon= ':smiley:')

# Method 2: Dictionary
PAGE_CONFIG = {"page_title":"KABI", "page_icon":":smiley", "layout": "centered"}
st.set_page_config(**PAGE_CONFIG)


st.title("Hello Streamlit ❤️ 😇 ")
st.sidebar.success("Menu")

  