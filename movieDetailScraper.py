import requests
import os
import random
from bs4 import BeautifulSoup
from urls import basic_url

def scrap_movie_detal(link):
    movieDetailList = []
    
    source = requests.get(link).text
    
    soup = BeautifulSoup(source,"lxml")
    
    
    
    
    