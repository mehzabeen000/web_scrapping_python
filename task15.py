import requests
from bs4 import BeautifulSoup
import json
import os
from pprint import pprint

file1 = open("all_over_movie_detail.json")
all_data = json.load(file1)

file2 = open("overall_cast.json")
cast_data = json.load(file2)

def analyse_actors():
    # unique_list =[]
    # new_list = []
    # for i in cast_data:
    #     for j in i:
    #         if j not in unique_list:
    #             unique_list.append(j)
    # # print(unique_list)

    # new_dict2 = {}
    # for i in unique_list:
    #     new_dict={}
    #     s_count = 0
    #     count = 0
    #     for j in cast_data:
    #         for k in j:
    #             if k==i:
    #                 count+=1
    #                 if count>1:
    #                     s_count = count
    #     new_dict["name"]=i["name"]
    #     new_dict["num_movies"]=s_count
    #     new_dict2[i["imdb_id"]]=new_dict
    # return new_dict2
    id_dict={}
    for i in all_data:
        for j in i["cast"]:
            id_dict[j["imdb_id"]]={}

    for i in all_data:
        for j in i["cast"]:
            for k in sorted(id_dict):
                if j["imdb_id"] in k:
                    id_dict[k]["name"]=j["name"]
                    id_dict[k]["num_movies"]=0

    for i in all_data:
        for j in i["cast"]:
            for k in sorted(id_dict):
                if j["imdb_id"] in k:
                    # id_dict[k]["name"]=j["name"]
                    id_dict[k]["num_movies"]+=1
   
    
    with open("task15.json","w") as t15:
        json.dump(id_dict,t15,indent=4)
    return id_dict
print(analyse_actors())