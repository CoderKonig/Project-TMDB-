import os
import requests
from flask import Flask, render_template
from tmdb import movie_details
import flask

from wiki import wikiLink


app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

movie_list = 372058, 27205, 496243

@app.route('/')
def index():
    
    #Passing variables in movie_details to flask
    title, tagline, genre, image = movie_details()
    # Wiki_URL variable allows me to pass title of the movie to wikiLink so that it can use the API to return a link
    Wiki_URL = wikiLink(title)
    return flask.render_template( "index.html", details= movie_details, title = title, tagline= tagline, genre= genre, image=image, wikiurl = Wiki_URL )



app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
    
)