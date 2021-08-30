import streamlit as st

#Summarization pkgs
# Text Rank Algorithm
from gensim.summarization import summarize

# LexRank Algorithm
from sumy.parses.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

#EDA Pkgs
import pandas as pd

# Data visualization
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') # Tkagg # Backend
import seaborn as sns

"""A Simple Summarizer App NLP App"""

st.title("Summarizer App")
menu = ["Home", "About"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Summarization")
    raw_text = st.text_area("Enter Text Here")
    if st.button("Summarize"):

        with st.expander("Original Text"):
            st.write(raw_text) 

    else:
        st.subheader("About")