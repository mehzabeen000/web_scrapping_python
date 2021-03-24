import requests
from bs4 import BeautifulSoup
import json
response = requests.get("https://webscraper.io/test-sites")
soup = BeautifulSoup(response.text,"html.parser")

list1 = []
div = soup.find("div",class_ = "container test-sites")
list_div = div.find_all("div")
for i in list_div:
    list_h2 = i.find_all("h2")
    for j in list_h2:
        list_a = i.find_all("a")
        for title in list_a:
            text = title.get_text().strip()
            list1.append(text)
print(list1)


