import streamlit as st
import gdown
from numpy import load

st.write('hello')

with st.spinner('downloading...'):
    if st.button('click to download'):
        url = "https://drive.google.com/u/0/uc?id=1Ws4NjZH0d5OiEor3hRbNziC0KeWi1Vjh&export=download"
        output = "scores.npy"
        gdown.download(url, output, quiet=False)
        st.write('successfully downloaded')

        similarity_matrix = load('scores.npy')

        st.write(similarity_matrix.shape)
