import requests
from bs4 import BeautifulSoup
import json
import os
import random,time
from pprint import pprint
file1 = open("task1.json")
m_name = json.load(file1)

def scrape_movie_details(url):
    random_ = random.randint(1,3)
    m_id = " "
    for i in url[27:]:
        if '/' not in i:
            m_id+=i
        else:
            break
    file_name = m_id+".json"
    text = None

    if os.path.exists(file_name):
        f = open(file_name)
        text = f.read()
        return text
    if text is None:
        time.sleep(random_)

    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    div = soup.find("div", class_ = "title-overview")

    n = div.find("div", class_ = "title_wrapper").h1.get_text()
    name= " "
    for i in n:
        if '(' not in i:
            name = name+i.strip()
        else:
            break
    director=[]
    direc = div.find("div",class_ = "credit_summary_item").a.get_text()
    director.append(direc)
    
    genre = div.find("div",class_ = "subtext").a.get_text()

    image_url = div.find("div",class_ = "poster").a["href"]
    poster_image_url = "https://www.imdb.com"+image_url

    sub_div = div.find("div", class_ = "subtext")
    run = sub_div.find('time').get_text().strip()
    run = run.replace("h"," ")
    run = run.replace("min"," ")
    hour = run[:3]
    mins = run[2:]
    if bool(mins) == False:
        mins = 0

    runtime = (int(hour)*60 + int(mins))

    bio = div.find("div", class_ = "summary_text").get_text().strip()
    
    div1 = soup.find("div", attrs= {"class":"article","id":"titleDetails"})
    list_div = div1.find_all("div")
    for i in list_div:
        list_h4 = i.find_all("h4")
        for j in list_h4:
            if "Language:" in j:
                list_a = i.find_all("a")
                for l in list_a:
                    language = l.get_text()

    country = div1.find("div",class_ = "txt-block").a.get_text()
    
    movie_dict_details = {"name":" ","director":" ","country":" ","language":" ","poster_image_url":" ","bio":" ","runtime":" ","genre":" "}
    movie_dict_details["name"]=name
    movie_dict_details["director"]=director
    movie_dict_details["country"]=country
    movie_dict_details["language"]=[language]
    movie_dict_details["poster_image_url"]=poster_image_url
    movie_dict_details["bio"]=bio
    movie_dict_details["runtime"]=runtime
    movie_dict_details["genre"]=[genre]
    

    with open(file_name,"w") as details:
        json.dump(movie_dict_details,details,indent = 4)
    return(movie_dict_details)

# url = m_name[0]["url"]
# m_detail = scrape_movie_details(url)
# print(m_detail)

def get_movie_list_details(movie_list):
    list1 = []
    for i in movie_list:
        detail = scrape_movie_details(i["url"])
        list1.append(detail)
    d = open("overall.json","w")
    r = json.dumps(list1,indent=4)
    d.write(r)
    d.close()
    return list1
movies_ = get_movie_list_details(m_name)
pprint(movies_)


