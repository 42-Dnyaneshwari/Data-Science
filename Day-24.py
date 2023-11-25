# -*- coding: utf-8 -*-
"""
Created on Wed May 17 08:20:52 2023

@author: Dnyaneshwari...
"""
##########################################
from fnmatch import fnmatch,fnmatchcase
names=['Dat1.csv','Dat2.csv','config.ini']
[name for name in names if fnmatch(name,'Dat*.csv')]
#output:['Dat1.csv', 'Dat2.csv']
################################


############################################3
#FNMATCH USED TO MATCH SOMETHING
from fnmatch import fnmatch,fnmatchcase
names=['Andheri East','East','Parle East','Dadar West']
[name for name in names if fnmatch(name,'* East')]
#output : ['Andheri East', 'Parle East']
###################################################


#################################################
#find out names ending with st
from fnmatch import fnmatch,fnmatchcase
addresses=[
            '5412 N Clerk St',
            '1060 W Addition St',
            '1039 W Gravial AVE',
            '5342 N Clerk St',
            '4587 N BRoad'
            ]
[i for i in addresses if fnmatch(i,'*St')]
#output: ['5412 N Clerk St', '1060 W Addition St', '5342 N Clerk St']
#################################################
import string
text='Yeah ,but no, but,Yeah,but,no,but,Yeah'
#exact Match
text=='Yeah' #False
#matching start or end
text.startswith('Yeah') #True
text.endswith('no') #False
#search the loc of 1st occurence of 'no'
text.find('no') #10
########################################


####################################
#use if u want to match a dates
text1='13/04/2004'
text2='Apr,13,2004'
import re
if re.match(r'\d+/\d+/\d+',text1):
    print('Yes...')
else:
    print("Nooo!!!!!!!!!")
#output: Yes...
if re.match(r'\d+/\d+/\d+',text2):
    print('Yes...')
else:
    print("Nooo!!!!!!!!!")
#output: Nooo!!!!!!!!!
#############################################


################################################
#re  package 
#datepat=re.compile(r'(\d+)/(\d+) 
num='333-444-5555'
if re.match(r'\d{3}-\d{3}-\d{4}',num):
    print('Yes')
else:
    print('nooo')
#output:Yes
################################################### 
