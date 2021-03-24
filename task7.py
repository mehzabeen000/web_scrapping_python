import requests
from bs4 import BeautifulSoup
import json
# from task5 import get_movie_list_details

file2 = open("ten_movies_detail.json")
ten_movies_detail = json.load(file2)

def analyse_movie_directors():
    dir_dict = {}
    dir_list = []
    for i in ten_movies_detail:
        l =  i["director"]
        l = l[0]
        dir_list.append(l)
    
    unique_dir= []
    for i in dir_list:
        if i not in unique_dir:
            unique_dir.append(i)

    for i in unique_dir:
        count = 0
        for j in dir_list:
            if i == j:
                count+=1
            dir_dict[i]=count

    with open("director.json","w") as dir_count:
        json.dump(dir_dict,dir_count,indent=4)
    return(dir_dict)

print(analyse_movie_directors())
