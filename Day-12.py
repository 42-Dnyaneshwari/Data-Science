# -*- coding: utf-8 -*-
"""
Created on Tue May  2 08:13:57 2023

@author: Nishant
"""

def add(a,b,c):
    sum=a+b+c
    return sum
print(add(3,5,7))

#lambda function
add=lambda a,b,c:a+b+c
print(add(3,5,7))
###########################
mul=lambda a,b,c:a*b*c
print(mul(3,5,7))
#############################

def person(name,**data):
    print(name)
    for i ,j in data.items():
        print(i,j)
person(name='navin',age='19',place='pune')