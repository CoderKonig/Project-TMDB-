# milestone2-iraj1
Project Milestone 2 Flask/TMDB 

## Implementation
- From the project planning side I mapped out all of the functionality I needed for flask login and writing to my database and had a skeleton of how everything would function together. During my implementation of these functions I ran into som eissues and had to redraw my skeleton for how things were passed and where they would be passing from.
- For the Register and Sign up functions I had originally had them in seperate py files and had tried to route the forms through the files, but decided to have everything inside my app.py to lessen my own confusion for where variables and forms where being directed to.


## Issues Solved
- Some of the issues I had faced were flask-login and how to implement it into my project, looking at the forms helped to an exstent but I had to watch a couple of tutorial videos to see how login manager was implemented.
- The next issue I faced was submitting my forms to the Database I created, homework 6 helped me greatly with reading and writing and I had to adjust my code a bit to make sure everything would work for this flask app. Reading from the database gave me alot of issues relating to jinja and not being able to iteralte through the length of an array of all the items in the database. Eventually debugging and seeing which pieces of code work and run by using print statements to show if my database was returning items I needed helped me figure the issue out.
- Finally I ran into alot of different errors with jinja and showing the reviews/ratings on the bottom of my page because there were variables that would not able to be iterated through to show all reviews, eventually tweaking with jinja helped me overcome the errors when returning my database and looking up jinja syntax.

## Copying this Repo and Running it on Your Machine

1. Clone the repo: git clone `https://github.com/csc4350-sp22/milestone2-iraj1.git`
2. After cloning the repo, you'll have to create a developer account at `https://www.themoviedb.org/`
3. Then you will have to register for an API Key for TMDB and have it stored in a secure location.
4. Open the cloned repo up and create a file called .env, here you will type in `TMDB_KEY= "Your_API_KEY"` and add your own `SECRET_KEY`.
5. Now you will be able to run the application locally by running `python3 app.py`.

If you choose to run it on Heroku:

6. You will then have to create a developer account at `www.heroku.com` AND install heroku on your machine by running 
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)`  # install Homebrew
`brew tap heroku/brew && brew install heroku`  # install Heroku CLI# install Heroku CLI

7. Login to Heroku using `heroku login -1`.
8. Create your own Heroku app by using `heroku create`.
9. Create a Postgres Database in heroku using `heroku addons:create heroku-postgresql: "app name"`
10. If you want to make changes to the code and run them on your own Heroku server then push your code with `git push heroku main`.
11. Add your own personal API key and the secret key to heroku dashboard in Settings and "Reveal config Vars".
12. Run `heroku open`.

13. You have successfuly ran an edited version of the repo on your own heroku serve.


Link to Heroku Website: `http://shrouded-falls-44837.herokuapp.com`


