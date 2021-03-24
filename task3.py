# import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
file1 = open("task1.json")
m_name = json.load(file1)

file2 = open("group_by_year.json")
group_detail = json.load(file2)

def group_by_decade():
    movie_decade={}
    decade_list =[]
    for year in group_detail:
        mode = int(year)%10
        decade = int(year)-mode
        if decade not in decade_list:
            decade_list.append(decade)
    k=0
    while k<len(decade_list):
        l=0
        k2 = decade_list[k]+10
        list1=[] 
        while l<len(m_name):
            if m_name[l]["year"]>=decade_list[k] and m_name[l]["year"]<k2:
                list1.append(m_name[l])
            movie_decade[decade_list[k]]=list1
            l+=1
        k+=1
    with open("group_by_decade.json","w") as group_by_year_decade:
        json.dump(movie_decade,group_by_year_decade,indent=4)
    return(movie_decade)
pprint(group_by_decade())