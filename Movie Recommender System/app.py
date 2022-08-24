import streamlit as st
import pickle
import pandas
import requests

st.set_page_config(page_title='Movie_Recommender', layout= "wide")
st.title("Movie Recommender System")

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

movie_df = pickle.load(open("movies.pickle", "rb"))
movies_list = movie_df["title"].values
similarity_df = pickle.load(open("similarity.pkl", "rb"))

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=930a5e2475c2d392aba57f5395ec93c1&language=en-US".format(movie_id))
    data = response.json()
    return  data["poster_path"]

def recommend_movie(movie):
    index = movie_df[movie_df["title"] == movie]["index"].values
    recommended_movie_index = similarity_df[similarity_df["i"].isin(index)].sort_values(by="value", ascending=False)["j"][1:9].values
    recommended_movie_id = movie_df[movie_df["index"].isin(recommended_movie_index)]["id"].values
    recommended_movie_name = movie_df[movie_df["index"].isin(recommended_movie_index)]["title"].values
    recommended_movie_poster = []
    counter = 0
    for id in recommended_movie_id:
        poster_path = fetch_poster(id)
        if poster_path is None:
            pass
        elif counter <= 5:
            recommended_movie_poster.append("https://image.tmdb.org/t/p/w500/" + poster_path)
            counter += 1
    return (recommended_movie_name, recommended_movie_poster)

selected_movie = st.selectbox(
'Which movie you have watched?', movies_list
)

if st.button('Recommend'):
     names, posters = recommend_movie(selected_movie)
     col1, col2, col3, col4, col5 = st.columns(5)

     with col1:
         st.text(names[0])
         st.image(posters[0])
    
     with col2:
         st.text(names[1])
         st.image(posters[1])
         
     with col3:
         st.text(names[2])
         st.image(posters[2])
     
     with col4:
         st.text(names[3])
         st.image(posters[3])
         
     with col5:
         st.text(names[4])
         st.image(posters[4])
