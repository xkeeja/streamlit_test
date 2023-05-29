import streamlit as st
import gdown
from numpy import load
import pandas as pd
from surprise import Dataset, Reader

st.write('hello')

with st.spinner('downloading...'):
    if st.button('click to download'):
        url = "https://drive.google.com/u/0/uc?id=1Ws4NjZH0d5OiEor3hRbNziC0KeWi1Vjh&export=download"
        output = "scores.npy"
        gdown.download(url, output, quiet=False)
        st.write('successfully downloaded .npy')

        similarity_matrix = load('scores.npy')

        st.write(similarity_matrix.shape)


        url_2 = "https://drive.google.com/u/0/uc?id=1Q_s55ingwAC4_vzAoJ3knXUqgExGpWzg&export=download"
        output_2 = "ScoresDF_selected.csv"
        gdown.download(url_2, output_2, quiet=False)
        st.write('successfully downloaded scores.csv')

        # st.dataframe(pd.read_csv('ScoresDF_selected.csv'))
        ScoresDF_selected = pd.read_csv('ScoresDF_selected.csv')



        url_3 = "https://drive.google.com/u/0/uc?id=1cq_0KRmQzb2bnOr9yVG019DETOUimA88&export=download"
        output_3 = "anime_cleaned.csv"
        gdown.download(url_3, output_3, quiet=False)
        st.write('successfully downloaded anime.csv')

        st.dataframe(pd.read_csv('anime_cleaned.csv'))


    def load_trainset():
        reader = Reader(rating_scale=(0, 10))
        scoredata = Dataset.load_from_df(ScoresDF_selected[['username', 'anime_id', 'my_score']], reader)
        trainset = scoredata.build_full_trainset()
        return trainset

    trainset=load_trainset()
