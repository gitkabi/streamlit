# Working Media files(video/images/audio)
# Display Images

import streamlit as st
from PIL import Image
img = Image.open("/home/kabigaruda/streamlit/image.jpg")
st.image(img, use_column_width = True)

# From URl
st.image("https://wallpapercave.com/wp/wp3105541.jpg")

# Display Videos
video_file = open("vid.mp4", "rb").read()
st.video(video_file, start_time = 1)

# Display Audio files
audio_file = open("/home/kabigaruda/streamlit/two.mp3", "rb")
st.audio(audio_file.read())