# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:53:14 2023

@author: Nishant
"""
users=['admin','employee','manager','worker','staff']
for i in users:
    if i=='admin':
        print("hello admin")
    elif i=='employee':
        print('hello employee')
    elif i=='manager':
        print("hello manager")
    elif i=='worker':
        print("hello worker")
    else:
        print("hello staff")
###########################################

cu=['ali','ram','sham','maya','gita']
nu=['ram','shreya','jibran','saili']
for i in nu:
    if i in cu:
        print("person will need to enter a new username")
    else:
        print("  saying that the username is available")
####################################################


# Python program to find the SHA-1 message digest of a file
# importing the hashlib module
##############################################

#ITERTOOLS
#NOW LET US START FROM 1
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))

#SUPOSE YOU HAVE REPEATED TASKS TO BE DONE 
#CYCLE

import itertools
ins=('eat','drink','sweet','code')
for ins in itertools.cycle(ins):
    print(ins)
##############################

#COMBINATIONS
from itertools import combinations
players=['john','rohit','virat','mahi']
for i in combinations(players,2):
    print(i)
##############################################

#use of fill value instead none
from itertools import zip_longest
name=['dada','kaka','mama','baba']
info=[2234,5675,2424,9594]
for nm , inf in zip_longest(name,info,fillvalue=2):
    print(nm,inf)
#####################################

#REPEAT
from itertools import repeat
for msg in repeat('keep short and krisp',times=3):
    print(msg)
#############################################3
 