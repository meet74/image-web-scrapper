import requests
import os
import random
from bs4 import BeautifulSoup



def scrap_movie(link):
    
    movieLinkList = []
    
    basic_url = "http://www.impawards.com"
    
    source = requests.get(link).text
    
    soup = BeautifulSoup(source, 'lxml')
    
    movieLink = soup.find_all("div",class_="constant_thumb")
    
    for m in movieLink:
       
        centerLink = m.find_all("center")
        if centerLink:
            #print(centerLink[0].find("a")["href"])
            movieLinkList.append(basic_url+centerLink[0].find("a")["href"])
    
    return movieLinkList
    
    
    
