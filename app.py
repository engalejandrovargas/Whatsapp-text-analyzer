import streamlit as st
import preprocess
import re
import stats
import matplotlib.pyplot as plt
import numpy as np


st.sidebar.title("Whatsapp Chat Analyzer")

# this is for uploading a file

uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()

    # converting the bytecode to the text-file

    data = bytes_data.decode("utf-8")

    # sending the file data to the preprocess function for further functioning

    df = preprocess.preprocess(data)

    # displaying the dataframe

    st.dataframe(df)

    
