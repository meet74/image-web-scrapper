import requests
from bs4 import BeautifulSoup
from urls import basic_url

def scrap_movie_detal(link, arr):
    
    
    source = requests.get(link).text
    
    soup = BeautifulSoup(source,"lxml")
    
    pTag = soup.find("p",class_="small")
    
    
    baseMovieDetailPageLink  = pTag.find("a")
    
    if baseMovieDetailPageLink:
       
         raw_base_movie_link =  link.split("com/")[1]
    
         base_movie_year = raw_base_movie_link[0:4]
    
         base_movie_link = basic_url+base_movie_year+"/"
         movieDetailPageLink = base_movie_link+baseMovieDetailPageLink["href"]
         
       
         get_poster_link(movieDetailPageLink,base_movie_link,arr)      
         
    else:
        return "NO LINK FOUND"



def get_poster_link(link,base_link,arr):
    response = requests.get(link).text
    
    soup = BeautifulSoup(response,"lxml")
    
    
    centerTag = soup.find("center")

   
    imgTag = centerTag.find("img")
    
    if imgTag:
        imageLink = base_link+centerTag.find("img")["src"]
        arr.append(imageLink)
       
        return imageLink
    else:
        return "No image Found"
       
   
    
    