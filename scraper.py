import requests
import os
import random
from bs4 import BeautifulSoup
from urls import basic_url
from movieScraper import scrap_movie
from movieDetailScraper import scrap_movie_detal

source = requests.get("http://www.impawards.com/alpha1.html").text


soup = BeautifulSoup(source, 'lxml')

movieList = []

htmlList = soup.find("ul", class_="pagination").findAll("li")

for li in htmlList:
    link = li.find("a")
    if link:
        movieList.append(basic_url+link["href"])


movieLinkListarr = scrap_movie(movieList[random.randrange(0,26)])

movie_poster_links = []


for links in movieLinkListarr:
    imageLink = scrap_movie_detal(links, movie_poster_links)
    
   

print(movie_poster_links)