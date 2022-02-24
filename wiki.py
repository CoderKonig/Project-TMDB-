#from turtle import title
from urllib import response
from tmdb import movie_details
import requests



# put title as an argument to help pass the movie title to this API
def wikiLink(title):
    WIKI_URL= 'http://en.wikipedia.org/w/api.php'


    params = {
        "action" : "opensearch",
        "search" :title,
        "namespace": "0",
        "limit": "5",
        "format": "json",
    }
    # Limit the movies to only 5 and using the open search API

    response= requests.get(url=WIKI_URL, params=params)
    #print out the first indicies and URL
    data = response.json()
    #URL ARRAY returns the 1st URL for each movie except Parasite(2019) 
    urlArray = data[3][0]
    parasiteArray = data

    #Parasite(2019) was the only movie that was not the 1st URL in the JSON
    #If statement to verify movie title and return the correct link
    if title == "Parasite":
        return parasiteArray[3][1]
        
    
    return urlArray
    



    

    


