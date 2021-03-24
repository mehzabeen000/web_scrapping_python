import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
# from task1 import scrap_top_list
# from task8 import get_movie_list_details

file1 = open("task1.json")
m_name = json.load(file1)

file2 = open("overall.json")
movie_detail = json.load(file2)

def analyse_language_and_directors():
    dir_dict = {}
    for i in movie_detail:
        for j in i["director"]:
            dir_dict[j]={}
    i=0
    while i<len(movie_detail):
        for j in dir_dict:
            if j in movie_detail[i]["director"]:
                for lang in movie_detail[i]["language"]:
                    dir_dict[j][lang]=0
        i+=1
    
    i=0
    while i<len(movie_detail):
        for j in dir_dict:
            if j in movie_detail[i]["director"]:
                for lang in movie_detail[i]["language"]:
                    dir_dict[j][lang]+=1
        i+=1
    with open("task10.json","w") as director_language:
        json.dump(dir_dict,director_language,indent=4)
    return(dir_dict)
    
pprint(analyse_language_and_directors())
