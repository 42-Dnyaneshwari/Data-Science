# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 09:10:42 2023

@author: Dnyaneshwari...
"""

#WEB SCRAPPING
#OFFFLINE WEBPAGE 
from bs4 import BeautifulSoup
import requests
soup=BeautifulSoup(open("C:/Users/Nishant/Pictures/sample_doc.html"),'html.parser')
#_______________________________________________________________________#

print(soup)
#getting all html code of the given webpage
#_______________________________________________________________________#

soup.text
#getting all the text present in the given webpage

soup.contents
#getting all the html contents extracted

soup.find("address")
#getting address
#<address> Mess on No. 72, Banamali Naskar Lane, Kolkata.</address>

soup.find_all("address")
#getting all address
#[<address> Mess on No. 72, Banamali Naskar Lane, Kolkata.</address>,
# <address>221B, Baker Street, London, UK.</address>]
#_______________________________________________________________________#


soup.find_all("q")
#getting all contains inside q tag
#[<q> There are more things in heaven and earth, Horatio, <br/> Than are dreamt of in your philosophy. </q>]
#_______________________________________________________________________#


soup.find_all("b")
#getting all contains inside b tag
#[<b>Sherlock </b>, <b>Hamlet</b>, <b>Horatio</b>]
#_______________________________________________________________________#


table=soup.find('table')
table
for i in table.find_all('tr'):
    columns=i.find_all('td')
    print(columns)
    table.find_all('tr')[3].find_all('td')[2]
    #it will show all the row except first row
#_______________________________________________________________________#
