import requests
import os
import random
from bs4 import BeautifulSoup
from urls import basic_url

def scrap_movie_detal(link, arr):
    
    
    source = requests.get(link).text
    
    soup = BeautifulSoup(source,"lxml")
    
    pTag = soup.find("p",class_="small")
    
    
    baseMovieDetailPageLink  = pTag.find("a")
    #print(baseMovieDetailPageLink)
    if baseMovieDetailPageLink:
        #  print(baseMovieDetailPageLink["href"])
         raw_base_movie_link =  link.split("com/")[1]
    
         base_movie_year = raw_base_movie_link[0:4]
    
         base_movie_link = basic_url+base_movie_year+"/"
         movieDetailPageLink = base_movie_link+baseMovieDetailPageLink["href"]
         
        #  print(base_movie_link)
        #  print(movieDetailPageLink)
         get_poster_link(movieDetailPageLink,base_movie_link,arr)
         
         
    else:
        return "NO LINK FOUND"



def get_poster_link(link,base_link,arr):
    response = requests.get(link).text
    
    soup = BeautifulSoup(response,"lxml")
    
    
    centerTag = soup.find("center")
    #print(base_link+centerTag.find("img")["src"])
   
    imgTag = centerTag.find("img")
    
    if imgTag:
        imageLink = base_link+centerTag.find("img")["src"]
        arr.append(imageLink)
       
        return imageLink
    else:
        return "No image Found"
       
   
    
#scrap_movie_detal("http://www.impawards.com/2017/aarons_blood_ver2.html")  
    
    