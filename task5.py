import requests
from bs4 import BeautifulSoup
import json
# from task1 import scrap_top_list
file1 = open("task1.json")
m_name = json.load(file1)

def get_movie_list_details():
    movie= m_name[:10]
    list1 = []
    for i in movie:
        url = i["url"]
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"html.parser")
        div = soup.find("div", class_ = "title-overview")
        n = div.find("div", class_ = "title_wrapper").h1.get_text()
        movie_dict_details = {"name":"  ","director":" ","country":" ","language":" ","poster_image_url":" ","bio":" ","runtime":" ","genre":" "}
        name= " "
        for i in n:
            if '(' not in i:
                name = name+i.strip()
            else:
                break

        director = div.find("div",class_ = "credit_summary_item").a.get_text()

        genre = div.find("div",class_ = "subtext").a.get_text()

        image_url = div.find("div",class_ = "poster").a["href"]
        poster_image_url = "https://www.imdb.com"+image_url

        sub_div = div.find("div", class_ = "subtext")
        run = sub_div.find('time').get_text().strip()
        run = run.replace("h"," ")
        run = run.replace("min"," ")
        hour = run[:2]
        mins = run[2:]
        runtime = int(hour)*60 + int(mins)

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
        
        
        movie_dict_details["name"]=name
        movie_dict_details["director"]=[director]
        movie_dict_details["country"]=country
        movie_dict_details["language"]=[language]
        movie_dict_details["poster_image_url"]=poster_image_url
        movie_dict_details["bio"]=bio
        movie_dict_details["runtime"]=runtime
        movie_dict_details["genre"]=[genre]
        list1.append(movie_dict_details)

    with open("ten_movies_detail.json","w") as details:
        json.dump(list1,details,indent = 4)
    return(list1)
    

get_movie_list_details()
    
