import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import random,time
import os
file1 = open("task1.json")
m_name = json.load(file1)

def scrape_movie_cast(url):
    random_ = random.randint(1,3)
    m_id = " "
    for i in url[27:]:
        if '/' not in i:
            m_id+=i
        else:
            break
    file_name = m_id+"_cast.json"
    text = None

    if os.path.exists(file_name):
        f = open(file_name)
        text = f.read()
        return text
    if text is None:
        time.sleep(random_)

    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    table = soup.find("table",class_ = "cast_list")
    actor = table.find_all("td",class_ = "")

    cast_list=[]
    for i in actor:
        actor_dict={}
        name = i.get_text().strip()
        imdb_id = i.find("a").get("href")[6:15]
        actor_dict["name"]=name
        actor_dict["imdb_id"]=imdb_id
        cast_list.append(actor_dict)
    with open(file_name,"w") as details:
        json.dump(cast_list,details,indent = 4)
    return(cast_list)
# print(scrape_movie_cast())

def get_cast_list_details(cast_list):
    list1 = []
    for i in cast_list:
        detail = scrape_movie_cast(i["url"]+"fullcredits?ref_=tt_cl_sm#cast")
        list1.append(detail)
    d = open("overall_cast.json","w")
    r = json.dumps(list1,indent=4)
    d.write(r)
    d.close()
    return list1
cast_ = get_cast_list_details(m_name)
pprint(cast_)
