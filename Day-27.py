# -*- coding: utf-8 -*-
"""
Created on Thu May 25 08:20:05 2023

@author: Dnyaneshwari...
"""
###############################################################
import unicodedata
t='----hello'
t.lstrip('-')
#output:'hello'

#character stripping
t='-----hellooo====='
t.lstrip('-')#'hellooo=====' left side special char removed
t.rstrip('=')#'-----hellooo' right side special char removed
t.strip('-=')#'hellooo' both side special char removed
############################################################
s=' hello world       \n'
s.strip()
s.replace(' ','')#'helloworld\n'
#concatenate two strings
############################################
import re
re.sub('\s+','',s)# 'hello world'
#removing whitespaces
###########################################
s = 'pýtĥöñ\fis\tawesome\r\n'
#clean the text use translte()
remap={
       ord('\t'):' ',
       ord('\f'):' ',
       ord('\r'):None #Deleted,
       }
a=s.translate(remap)
print(a)#pýtĥöñ is awesome
##################################################

import unicodedata
import sys
cmb_chrs=dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b=unicodedata.normalize('NFD',a)
print(b)     #pýtĥöñ is awesome
b.translate(cmb_chrs)   #'python is awesome\n'
#####################################################

#IO encoding and encoding function
#cleanup the text and run it using encode() and decode()
a = 'pýtĥöñ is awesome\n'
b=unicodedata.normalize('NFD',a)
b.encode('ascii','ignore').decode('ascii')
#'python is awesome\n'

#############################################################

#aligining the text
text='Hello World'
text.ljust(20)#'Hello World         '
text.rjust(20)# '         Hello World'
text.center(20)#'    Hello World     '

###############################################

#Add character and special symbol
text.ljust(20,'=')#'Hello World========='
text.rjust(20,'+')#'+++++++++Hello World'
text.center(20,'*')#'****Hello World*****

##################################################

format(text,'>20')#'         Hello World'
format(text,'<20')#'Hello World         '
format(text,'^20')#'    Hello World     '

################################################

format(text,'=>20')#'=========Hello World'
format(text,'+<20')#'Hello World+++++++++'
format(text,'*^20')#'****Hello World*****'

##############################################
#we use format()
'{:>10s}{:<10s}'.format('Hello','World')
#'     HelloWorld     '
###################################################
x=1.2345
format(x,'>10')#'    1.2345'
format(x,'^10.2f')#'   1.23   '
#####################################
parts=['Is','Chicago','Not','Chicago?']
' '.join(parts)
#'Is Chicago Not Chicago?'
','.join(parts)
#'Is,Chicago,Not,Chicago?'
''.join(parts)
#'IsChicagoNotChicago?'
#if u join very few
a='Is Chicago'
b='Not Chicago?'
a + ' ' + b
#'Is Chicago Not Chicago?'
print('{} {}'.format(a,b))
#Is Chicago Not Chicago?
##############################
a='Hello' 'World'
a
#'HelloWorld'
a='Hello'' ''World'
a
#'Hello World'
#####################################
#interpolating variables in strings
#string represents a value of a variable
s='{name} has {n} messages'
s.format(name='Dnyaneshwari',n=42)
#'Dnyaneshwari has 42 messages'
name='Dnyaneshwari'
n=42
s.format_map(vars())
#'Dnyaneshwari has 42 messages'
###################################################
#Indentation or text Wraping

import textwrap
s='1. The Clearance form, for submission has, been created for the students. \
Student need ,to collect the form from ,class coordinator\
Students have to, take the signature of the class, coordinator and \
'
print(textwrap.fill(s,70,initial_indent='   '))
#output
'''
1. The Clearance form, for submission has, been created for the
students. Student need ,to collect the form from ,class
coordinatorStudents have to, take the signature of the class,
coordinator and
'''
print(textwrap.fill(s,70,subsequent_indent='   '))
'''
1. The Clearance form, for submission has, been created for the
   students. Student need ,to collect the form from ,class
   coordinatorStudents have to, take the signature of the class,
   coordinator and

'''
####################################################
