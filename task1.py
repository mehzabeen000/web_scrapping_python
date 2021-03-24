import requests
from bs4 import BeautifulSoup
import json
page = requests.get("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in")
soup = BeautifulSoup(page.text,"html.parser") 
def scrap_top_list():
    div = soup.find("div", class_ = "lister")
    table = div.find("tbody", class_="lister-list" )
    tr = table.find_all("tr")

    movie_name=[]
    movie_year=[]
    movie_rank =[]
    movie_url =[]
    movie_rating=[]
    for i in tr:
        details = i.find("td",class_="titleColumn").get_text().strip()
        rank = " "
        j=0
        while j<len(details):
            if "." not in details[j] :
                rank+=details[j]
            else:
                break
            j+=1
        movie_rank.append(rank)

        name = i.find("td",class_="titleColumn").a.get_text()
        movie_name.append(name)

        year = i.find("td",class_="titleColumn").span.get_text()
        movie_year.append(year)

        rating = i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        movie_rating.append(rating)

        url = i.find("td",class_="titleColumn").a["href"]
        url_add = "https://www.imdb.com"+url
        movie_url.append(url_add)
    
    movie_list=[]
    movie_dict = {"rank":" ","name":" ","year":" ","rating":" ","url":" "}
    i=0
    while i<len(movie_rank):
        movie_dict["rank"]=int(movie_rank[i])
        movie_dict["name"]=movie_name[i]
        movie_dict["year"]=int(movie_year[i][1:5])
        movie_dict["rating"]=float(movie_rating[i])
        movie_dict["url"]=movie_url[i]
        movie_list.append(movie_dict.copy())
        i+=1
    
    with open("task1.json","w") as movie_data:
        json.dump(movie_list,movie_data,indent=4)
    return(movie_list)
scrap_top_list()



