import os
import random
import requests
#from wiki import wikiLink
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) # This is to load your API keys from .env


TMDB_KEY = os.getenv("TMDB_KEY")

# Parasite (496243)
# Your Name = 372058
# Inception = 27205


CONFIG_URL = "https://api.themoviedb.org/3/configuration?api_key={API_KEY}" . format(API_KEY= TMDB_KEY)


def movie_details():
    #Put the Base URL inside the function so I can do random.choice for the list of Movie ID's 
    movie_list = 372058, 27205, 496243
    movie_id= random.choice(movie_list)
    BASE_URL = "https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}" . format(movie_id= movie_id, API_KEY=TMDB_KEY)

    params = {'api-key': os.getenv('TMDB_KEY')}
    response = requests.get(BASE_URL)

    data= response.json()


    #the below function get_genre is basically getting the names from inside the Genres Array
    genreName= data['genres']
    def get_genre(name):
        return name['name']

    
    genre= map(get_genre, genreName)
    
    #grabbing the image and the poster path to preview the image for each movie
    image = "https://image.tmdb.org/t/p/w500" + data['poster_path']


    #title and tagline were both items in the array that were easily returned
    title = response.json()["title"]
    tagline = response.json()["tagline"]

    return (title, tagline, list(genre), image, movie_id )
