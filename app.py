import pickle
import streamlit as st
import requests

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

def recommender_system(movie):
  movies_index = movies_tag[movies_tag['original_title'] == movie].index[0]

  dist = cos_sim[movies_index]

  movies_list = sorted(list(enumerate(dist)), reverse = True, key = lambda x:x[1])[1:5]

  for movie in movies_list:
    return (movies_tag.iloc[movie[0]].original_title)


st.header('Movie Recommender System')
movies = pickle.load(open('model/movie_tags.pickle','rb'))
similarity = pickle.load(open('model/similarity.pickle','rb'))

movie_list = movies['original_title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(recommended_movie_names[0])
    with col2:
        st.text(recommended_movie_names[1])

    with col3:
        st.text(recommended_movie_names[2])

    with col4:
        st.text(recommended_movie_names[3])

    with col5:
        st.text(recommended_movie_names[4])
