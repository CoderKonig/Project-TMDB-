import os
import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from tmdb import movie_details
import flask
from dotenv import load_dotenv, find_dotenv
from wiki import wikiLink


load_dotenv(find_dotenv())

app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# Gets rid of a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    messages = db.Column(db.String(400), nullable=False)
    rating = db.Column(db.String(120), nullable=False)

db.create_all()

movie_list = 372058, 27205, 496243

@app.route('/')
def index():
     return flask.render_template("login.html")


@app.route('/signin', methods = ["GET","POST"])
def signin():
    title, tagline, genre, image = movie_details()
    # Wiki_URL variable allows me to pass title of the movie to wikiLink so that it can use the API to return a link
    Wiki_URL = wikiLink(title)
    


    if flask.request.method == "GET":
        # data = flask.request.form
        # userExists = Users(username= data["userName"])
        u_name = flask.request.form.get('username')
        p_word = flask.request.form.get('password')
        if Users.query.filter(Users.userName == u_name & Users.password == p_word ):
            return flask.render_template( "index.html", details= movie_details, title = title, tagline= tagline, genre= genre, image=image, wikiurl = Wiki_URL )


    return flask.render_template( "index.html", details= movie_details, title = title, tagline= tagline, genre= genre, image=image, wikiurl = Wiki_URL )


#Create a method for Register, type in username and password and the DB records the Username

@app.route('/register', methods = ["GET","POST"])
def register():

    if flask.request.method == "POST":
        newUserForm = flask.request.form.get('username')
        newUser = Users(username= newUserForm["userName"])
        # Flask form for Username 
        db.session.add(newUser)
        db.session.commit()
    
    
       

    return signin()



# Original App Route for Movie Info Below


#     #Passing variables in movie_details to flask
#     title, tagline, genre, image = movie_details()
#     # Wiki_URL variable allows me to pass title of the movie to wikiLink so that it can use the API to return a link
#     Wiki_URL = wikiLink(title)
#     return flask.render_template( "index.html", details= movie_details, title = title, tagline= tagline, genre= genre, image=image, wikiurl = Wiki_URL )



app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
    
)

#git push heroku main