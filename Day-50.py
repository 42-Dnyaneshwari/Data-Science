# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 08:47:44 2023

@author: Dnyaneshwari
"""
#whenever write abput class use : class_=
#web scrpping the online page 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import requests
from bs4 import BeautifulSoup 

#_______________________________________________________________________#


url="https://sanjivanicoe.org.in/index.php/contact"
req=requests.get(url)
req
#response 200 connection is established
soup=BeautifulSoup(req.content)
soup
soup.prettify()
#the text is neat and clean
list(soup.children)
#finding all content using tab

#_______________________________________________________________________#

#accesssing info usING CLASS TAB

soup.find_all('p')
#getting all contents of p tag

soup.find_all('p')[1].get_text()#'Nearest Railway Station- Kopargaon (1Km)'
#getting content of p tag but only first row

soup.find_all('p')[2].get_text()#'Nearest Airport - Shirdi (10Km)'
#getting content of p tag but only first row

#_______________________________________________________________________#



