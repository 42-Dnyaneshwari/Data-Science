# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:26:35 2023

@author: Dnyaneshwari...
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import requests
from bs4 import BeautifulSoup 

#_______________________________________________________________________#

url="https://www.flipkart.com/apple-iphone-15-plus-blue-256-gb/p/itm4f3e6fe529a68?pid=MOBGTAGPZXR7SRP6&lid=LSTMOBGTAGPZXR7SRP6LPK3EE&marketplace=FLIPKART&q=iphone+15+plus&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_HistoryAutoSuggest_1_1_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_1_na_na_na&fm=organic&iid=2ab3c66e-6028-4fb8-9acb-f870d8debfe3.MOBGTAGPZXR7SRP6.SEARCH&ppt=clp&ppn=the-big-billiondays-2023-top-deals-from-house-of-samsung-kgf92e-store&ssid=un54m8qm4w0000001699280145188&qH=72d286a378c732d0"
req=requests.get(url)
req
#response 200 connection is established
soup=BeautifulSoup(req.content)
soup

soup=BeautifulSoup(req.content,'html.parser')
soup
soup.prettify()
#_______________________________________________________________________#

#accesssing info usING CLASS TAB

title=soup.find_all('div',class_='')
title
review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text)
review_title
len(review_title)
rating=soup.find_all('div',class_='')










