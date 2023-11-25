# -*- coding: utf-8 -*-
"""
Created on Tue May 23 08:56:58 2023

@author: Dnyaneshwari...
"""
#########################################################
import re
import nltk
text='UPPER PYTHON,lower python ,MixeD PythoN'
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
re.sub('python', matchcase('Snake'),text,flags=re.IGNORECASE)       
#output
#'UPPER SNAKE,lower snake ,MixeD Snake'
##############################################

str_pat=re.compile(r'\"(.*)\"')
txt1='Computer say "Noo."'
str_pat.findall(txt1)
#output  ['Noo.']


str_pat=re.compile(r'\"(.*)\"')
txt2='Computer say "Noo." Phones say "Yes."'
str_pat.findall(txt2)
#output      ['Noo." Phones say "Yes.']

str_pat=re.compile(r'\"(.*?)\"')
txt2='Computer say "Noo." Phones say "Yes."'
str_pat.findall(txt2)
#output      ['Noo.' , 'Yes.']
#######################################################
#WEB SCRAPPING
#for single line comment we use
comment=re.compile(r'/\*(.*?)\*/')
txt2='/* this is a comment*/'
comment.findall(txt2)
#output   [' this is a comment']

#for multiline comment we use
comment=re.compile(r'/\*((?:.|\n)*?)\*/')
txt2='''
/* This Is A Multiline  Comment*/
'''
comment.findall(txt2)
#output [' This Is A Multiline  Comment']
###############################################
import re
def remove_num(text):
    res=re.sub(r'\d+','',text)
    return res
str='there are  3 balls in this bags, and 12 in the cup '
remove_num(str)
#output: all digit have been removed
# 'there are   balls in this bags, and  in the cup '
##################################
#number to convert with 
import inflect
p=inflect.engine()
#convert no to word
def convert_num(text):
    temp_str=text.split()
    #initialise empty list
    new_string=[]
    for word in temp_str:
        #if word is a digit then convert it into word
        if word.isdigit():
            temp=p.number_to_words(word)
            new_string.append(temp)
            #append the word as it is
        else:
            new_string.append(word)
#join the word of new_string and string
    temp_str=' '.join(new_string)
    return temp_str
input_str='there are  3 balls in this bags, and 12 in the cup '
convert_num(input_str)
#output
#'there are three balls in this bags, and twelve in the cup'

#########################################################
#EXERCISE 1
#reverse a string
str='my name is Dnyaneshwari'
print(str[::-1]) #irawhsenaynD si eman ym
#orrrrr
str='my name is Dnyaneshwari'
#Use the split() mwthod to split a string into a list of 
#reverse each word from a list
#finally, use the join() function to convert a list into
def reverse_words(string):
    words = string.split()  # Split the string into a list of words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    reversed_string = ' '.join(reversed_words)  # Join the reversed words back into a string
    return reversed_string
reverse_words(str)
#output:'ym eman si irawhsenaynD'
####################################################

#EXERCISE 2
'''
read the txt file and store it in working directory
File Input:
line1
line2
expected output:line1 line2
use replace() and replaceall()
'''
with open('C:/1-Python/sample.txt','r')as file:
    obj=file.read()
    print(obj)
obj.replace("\n"," ")
#output:'My Name Is Dnyaneshwari'
#realpython.com  study it:)
 