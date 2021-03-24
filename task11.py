import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

file1 = open("task1.json")
m_name = json.load(file1)

file2 = open("overall.json")
movie_detail = json.load(file2)

def analyse_movies_genre(movie_detail):
    genre_dict = {}
    for i in movie_detail:
        for j in i["genre"]:
            genre_dict[j]={}

    i=0
    while i<len(movie_detail):
        for j in genre_dict:
            if j in movie_detail[i]["genre"]:
                    genre_dict[j]=0
        i+=1
    
    
    i=0
    while i<len(movie_detail):
        for j in genre_dict:
            if j in movie_detail[i]["genre"]:
                    genre_dict[j]+=1
        i+=1
    with open("task11.json","w") as genre_count:
        json.dump(genre_dict,genre_count,indent=4)
    return(genre_dict)
    
pprint(analyse_movies_genre(movie_detail))
