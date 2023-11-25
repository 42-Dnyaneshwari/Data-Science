# -*- coding: utf-8 -*-
"""
Created on Tue May 16 08:05:46 2023

@author: Dnyaneshwari...
"""
#python for Natural Language Processing
#DS:1)NLP 2)visualisation 3)reinforcement
#NLP(Natutal Language Processing)
#text & voice processing
##############################################

#tokenization = seperating words
txt='welcome to the new year 2023'
x=txt.split()
print(x)
#output
#['welcome', 'to', 'the', 'new', 'year', '2023']
#removing sepacial character
#eg. #,!,?
##############################################

#######################################
import re
def remove_special_character(text):
    #define a pattern to keep eg pat
    pat=r'[^a-zA-z0-9.,!?/:;"\'\s]'
    return re.sub(pat,' ',text)
remove_special_character('007 Not sure@ if this % was #fun! 58544 what do#')
#it removes all special char except pat var
############################################


###############################################
#Removing Numbers
def remove_numbers(num):
    pat=r'[^a-zA-z.,!?/:;"\'\s]'
    return re.sub(pat,' ',num)
remove_numbers('007 Not sure@ if this % was #fun! 58544 what do#')
#yes it have remove all the numbers from text
############################################


#now it will not consider passed special char
#| | between them not to keep
txt='welcome to the new year; 2023!'
import re
x=re.split(r'(?:,/;|\s)s*',txt)
print(x)
###################################

#######################################
#remove punctuation
#funtion for removing puncuation
import string
def rem_punctuation(text):
    text=''.join([c for c in text if c not in string.punctuation])
    return text
rem_punctuation('Article! @first sentence of some ,{importtant} article')
#output:it have remove all puntuation

#'Article first sentence of some important article'

#preprocessing: sentences:words:puncutation:special char

#stemming:process of reducing the derive words to there root words
#eg eating : eat
# pip install nltk

import nltk
def get_Stem(text):
    stemmer = nltk.porter.PorterStemmer()
    text=' '.join([stemmer.stem(word) for word in text.split()])
    return text
get_Stem('we are eating and dancing ; he eating and swimming ; we have been eating and swimming')
#output below
# 'we are eat and danc ; he eat and swim ; we have been eat and swim'
####################################################

#
line='asdf fjdk fjek,asdk,foo'
re.split(r'(/?:,|;|\s)\s*',line)
#define not to keep
pattern=r'(?:,|;|\s)\s*'
x=re.split(pattern,txt)
print(x)
# output : ['welcome', 'to', 'the', 'new', 'year', '2023']
##################################################

#matching text at the start or end of string
filename='spam.txt'
filename.endswith('.txt') #True
#######################################
area_name='6 th lane west Andheri'
area_name.endswith('west Andheri') #True
########################################

choices=('https:','ftp:')
url='https:/www.goggle.org'
url.startswith(choices)
#output: True
##########################################

#slicing a string
# $ [start:end:step]
#default index starts with 0
s='ABCDEFGHI'
print(s[0::1]) #ABCDEFGHI
print(s[2:7]) #CDEFG
print(s[-7:-2:])#CDEFG 
print(s[2:-5]) #CD ie start with 2 and go upto -4
#with step
print(s[2:7:2]) #CEG
print(s[6:1:-2]) #GEC
print(s[:3]) #ABC
#s[start:len]
print(s[6:]) #GHI
#########################################

#reverse a string
print(s[::-1]) #IHGFEDCBA
#################################

filename='spam.txt'
filename[-4:]=='.txt'
#True
####################################
url='https://www.goggle.org'
url[:5]=='http:' #False i.e. 5 se aage tak
url[:6]=='https:' #True i.e 6 se aage tak
url[:4]=='http' #True 4 se aage tak
url[:5]=='https:' or url[:6]=='https:' or url[:4]=='https:'
#True
#################################################