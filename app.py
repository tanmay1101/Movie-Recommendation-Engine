# Importing essential liberaries
import pandas as pd
import streamlit as st   # is an open-source app framework to create web apps for ML
import pickle
import requests  # to send HTTP requests
#import style as style  # for styling out web app
from PIL import Image   # to read image# Importing essential liberaries
import pandas as pd
import streamlit as st   # is an open-source app framework to create web apps for ML
import pickle
import requests  # to send HTTP requests
import style as style  # for styling out web app
from PIL import Image   # to read image

# Loading model and dataset that we have created in juyter notebook
movies = pickle.load(open('movies.pkl', 'rb'))
similarity= pickle.load(open('similarity.pkl', 'rb'))


# Defining a function fetch_poster that will return movie poster from tmdb through api
def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d14e00e86623e87443e17a950d03828b&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']


# Defining a function which will return 5 similar movies and their poster based on similarity and tmdb api
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # getting movie index
    distances = similarity[movie_index]  #calculating distance of each other movies from title
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  # getting top 5 movies with minimum distance

    recommended_movies= []   # creating an empty list of recommended movies
    recommended_movies_poster=[]  # creating an empty list of recommended movies posters

    # We will append movie_list and poster one by one in above list
    for i in movies_list:

        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch movies poster from tmdb api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster



### Creating frondend of web app that will take a movie as a input and return list of movies that we created
st.title('Movie Recommender System')      # Giving title of our app
image = Image.open('movie.jpg')
st.image(image, width= 1000, use_column_width= True)

selected_movie_name = st.selectbox(
 'Please input your favourite movie...',
 movies['title'].values)

### Creating a button that will give all 5 movies and their poster
if st.button('Recommend'):
   'We recommend you to watch below 5 movies to watch.....'
   recommended_movie_names, recommended_movie_posters= recommend(selected_movie_name)
   col1, col2, col3, col4, col5 = st.beta_columns(5)
   'Thanks for your interest. This app is created by Tanmay Dwivedi'
   with col1:
       st.text(recommended_movie_names[0])
       st.image(recommended_movie_posters[0])
   with col2:
       st.text(recommended_movie_names[1])
       st.image(recommended_movie_posters[1])

   with col3:
       st.text(recommended_movie_names[2])
       st.image(recommended_movie_posters[2])
   with col4:
       st.text(recommended_movie_names[3])
       st.image(recommended_movie_posters[3])
   with col5:
       st.text(recommended_movie_names[4])
       st.image(recommended_movie_posters[4])