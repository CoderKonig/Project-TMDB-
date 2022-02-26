import os
from flask_login import(login_user, LoginManager,login_required, logout_user,current_user,) 
import requests
from flask import Flask, flash, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from tmdb import movie_details
import flask
from dotenv import load_dotenv, find_dotenv
from wiki import wikiLink


load_dotenv(find_dotenv())

app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")   

# Gets rid of a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(120), nullable=False)

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    messages = db.Column(db.String(400), nullable=False)
    rating = db.Column(db.String(120), nullable=False)

# db.create_all()

movie_list = 372058, 27205, 496243

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "signin"

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route('/', methods=["GET", "POST"])
@login_required
def index():
    if flask.request.method == "POST":
        data = flask.request.form
        # newUserForm = 
        newUser = Users(userName= data["r_username"] )
        # newPass = Users(password= data["r_password"])

        # Flask form for Username 
        db.session.add(newUser)
        db.session.commit()
    
    return flask.render_template( "login.html")


@app.route('/signin', methods = ["GET","POST"])
def signin():
    title, tagline, genre, image, movie_id = movie_details()
    # Wiki_URL variable allows me to pass title of the movie to wikiLink so that it can use the API to return a link
    Wiki_URL = wikiLink(title)
    
    if flask.request.method == "POST":
        
        print(flask.request.form.get('username'))
        u_name= flask.request.form.get('username')
        if Users.query.filter_by(userName=u_name).first():
            print("User Found")
            return flask.render_template( "index.html", details= movie_details, title = title, tagline= tagline, genre= genre, image=image, wikiurl = Wiki_URL, movie_id=movie_id )
            
        else:  
            flask.flash("User Not Found")
            print("User not found", u_name)
            return flask.render_template("login.html")


    return flask.render_template("login.html")


@app.route('/reviews', methods=["POST"])
def review():
    title, tagline, genre, image, movie_id = movie_details()
    # Wiki_URL variable allows me to pass title of the movie to wikiLink so that it can use the API to return a link
    Wiki_URL = wikiLink(title)
    if flask.request.method =="POST":


        # user = current_user.user
        data = flask.request.form
    
        review = flask.request.form.get('comment')
        rating = flask.request.form.get('rating')
        id = flask.request.form.get('movie_id')

        new_review = Reviews(messages= review,rating= rating)
        db.session.add(new_review)
        db.session.commit()
    AllReviews= Reviews.query.all()
    listComments= len(AllReviews)

    # reviews = Reviews.query.all()
    # lengthreviews = len(reviews)
    return flask.render_template( "index.html",
     details= movie_details, 
     title = title, 
     tagline= tagline, 
     genre= genre, 
     image=image, 
     wikiurl = Wiki_URL,
     movie_id=movie_id,
     AllReviews = AllReviews,
     listComments = listComments
      )
    #  reviews= reviews, 
    #  lengthreviews=lengthreviews )



app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
    
)

#git push heroku main