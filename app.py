import streamlit as st
import gdown
from numpy import load
import pandas as pd
import pickle

st.write('hello')

with st.spinner('downloading...'):
    if st.button('click to download'):
        url = "https://drive.google.com/u/0/uc?id=1Ws4NjZH0d5OiEor3hRbNziC0KeWi1Vjh&export=download"
        output = "scores.npy"
        gdown.download(url, output, quiet=False)
        st.write('successfully downloaded .npy')

        similarity_matrix = load('scores.npy')

        st.write(similarity_matrix.shape)


        url_2 = "https://drive.google.com/u/0/uc?id=1fx_XfWa8e-sx5j5N5SCo4GHpMDBImFLo&export=download"
        output_2= "trainset.obj"
        gdown.download(url_2, output_2, quiet=False)
        st.write('successfully downloaded trainset.obj')

        # st.dataframe(pd.read_csv('ScoresDF_selected.csv'))
        # ScoresDF_selected = pd.read_csv('ScoresDF_selected.csv')



        url_3 = "https://drive.google.com/u/0/uc?id=1cq_0KRmQzb2bnOr9yVG019DETOUimA88&export=download"
        output_3 = "anime_cleaned.csv"
        gdown.download(url_3, output_3, quiet=False)
        st.write('successfully downloaded anime.csv')

        # st.dataframe(pd.read_csv('anime_cleaned.csv'))


        f=open('trainset.obj', 'rb')
        trainset=pickle.load(f)
        f.close()
