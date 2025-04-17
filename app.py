import streamlit as st
import pandas as pd
import pickle
from  util_1 import set_background_image,image_url,fetch_poster,literal_eval
set_background_image(image_url)



def fetching_poster(select_movie):
    Id=movies_data[movies_data['title'] == select_movie]['movie_id'].values[0]
    path=fetch_poster(Id)
    return path







movie_list = pickle.load(open('data_\movies_data.pkl','rb'))
movies_data = pd.DataFrame(movie_list)

select_movie=st.selectbox(
    "Search Movie Title",
    movies_data['title'].values,
    index=None,
    placeholder="Search...",
)
if(select_movie!=None):
    col1, col2 = st.columns(2)
    with col1:
        st.image(fetching_poster(select_movie),width=200,caption=select_movie)
    
    with col2:
        st.markdown(f"Title: {select_movie}")
        st.markdown(f"Release Date: {movies_data[movies_data['title'] == select_movie]['release_date'].values[0]}")
        st.markdown(f"Director: {literal_eval(movies_data[movies_data['title'] == select_movie]['crew'].values[0])}")
        st.markdown(f"Cast: {literal_eval(movies_data[movies_data['title'] == select_movie]['cast'].values[0])}")
        st.markdown(f"Genres: {literal_eval(movies_data[movies_data['title'] == select_movie]['genres'].values[0])}")
        st.markdown(movies_data[movies_data['title'] == select_movie]['overview'].values[0])