import requests
from bs4 import BeautifulSoup
import json
import os
from pprint import pprint

file1 = open("task1.json")
m_name = json.load(file1)

file2 = open("overall_cast.json")
cast_data = json.load(file2)

file3 = open("overall.json")
movie_data = json.load(file3)

def scrape_movie_details():
    dict_new={}
    new_list=[]
    i=0
    while i<len(movie_data):
        dict_new=movie_data[i]
        dict_new["cast"]=cast_data[i]
        new_list.append(dict_new)
        i+=1
    with open("all_over_movie_detail.json","w") as combo:
        json.dump(new_list,combo,indent=4)
    return new_list

print(scrape_movie_details())



