import requests
from bs4 import BeautifulSoup
import json
# from task5 import get_movie_list_details
file2 = open("ten_movies_detail.json")
ten_movies_detail = json.load(file2)

def analyse_movie_language():
    lang_dict = {}
    lang_list = []
    for i in ten_movies_detail:
        l =  i["language"]
        l = l[0]
        lang_list.append(l)
    
    unique_lang= []
    for i in lang_list:
        if i not in unique_lang:
            unique_lang.append(i)

    for i in unique_lang:
        count = 0
        for j in lang_list:
            if i == j:
                count+=1
            lang_dict[i]=count

    with open("language.json","w") as lang_count:
        json.dump(lang_dict,lang_count,indent=4)
    return(lang_dict)

print(analyse_movie_language())
