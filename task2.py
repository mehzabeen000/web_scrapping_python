import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

file1 = open("task1.json")
m_name = json.load(file1)

group_by_year_dict={}
def group_by_year():
    years=[]
    for i in m_name:
        year = i["year"]
        years.append(year)
    i=0
    years_once=[]
    while i<len(years):
        if years[i] not in years_once:
            years_once.append(years[i])
        i+=1
    years_once.sort()
    k=0
    while k<len(years_once):
        l=0
        list1=[] 
        while l<len(m_name):
            if years_once[k]==m_name[l]["year"]:
                list1.append(m_name[l])
                
            group_by_year_dict[years_once[k]]=list1
            l+=1
        k+=1
    with open("group_by_year.json","w") as group_year_detail:
        json.dump(group_by_year_dict,group_year_detail,indent=4)
    return(group_by_year_dict)
pprint(group_by_year())
