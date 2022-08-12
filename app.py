import streamlit as st
import pandas as pd
import numpy as np
import pickle

moviesDetail = pickle.load(open('moviesDetail.pkl','rb'))
moviesList = moviesDetail.title.values

similarity = pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
    index = moviesDetail[moviesDetail['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True,key = lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(moviesDetail.iloc[i[0]].title)
    return recommended_movies

st.title('Movie Recommendation System')

selected_movie = st.selectbox('Pick one', moviesList)

if st.button('Recommend'):
    for i in recommend(selected_movie):
        st.write(i)

