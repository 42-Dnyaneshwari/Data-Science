
import pandas as pd
f1=pd.read_csv('C:/1-Python/buzz.csv')
###########################################
#opening file as a row data
import os
with open('buzz.csv')as row_data:
    print(row_data.read())
####################################
#Reading cvs data as a list
import csv
with open('buzz.csv') as row_data:
    for line in csv.reader(row_data):
        print(line)
####################################
#reading csv file as a dictionary
import csv
with open('buzz.csv') as row_data:
    for line in csv.DictReader(row_data):
        print(line)
#########################################
with open('buzz.csv') as data:
    f={}
    for line in data:
        k,v=line.split(',')
        f[k]=v
f
################################################
#stripping then spliting your row data
with open('buzz.csv') as data:
    ignore=data.readline()
    f={}
    for line in data:
        k,v=line.strip().split(',')
        f[k]=v
f
###################################################
#flask and decoraters
#decoraters
def plus_one(n):
    return n+1
plus_one(6)
############################################
#function inside function
def plus_one(n):
    def add_one(n):
        return n+1
    res=add_one(n)
    return res
plus_one(6)
############################################
#passing function as a parameter to another function
def plus_one(n):
    return n+1

def fun_call(fun):
    res=fun(5)
    return res
fun_call(plus_one)
#############################################
#function returnning other function
#it is mandetory to assign function to a variable
def hell():
    def say():
        return 'Hii'
    return say()
h=hell()
hell()
#remember
#when u call hell function directly then it will show obj 
#that is why u need assign it to the var to the hell()