# -*- coding: utf-8 -*-
"""
Created on Wed May 10 08:20:59 2023

@author: Dnyaneshwari...
"""

#Pandas Series
#series is a 1D data
#DataFrame is 2D data
import pandas as pd
 
################################################

##############################################
songs3=pd.Series([145,142,38,13],name='counts',
                 index=['paul','John','George','Rango'])
songs3.index
print(songs3)
###################################################

#Nan is stands for Not a Number
#and it is usually ignored in arithmatic
#similer to NULL in SQL
#numeriac column will be nan
import numpy as np
numpy_ser=np.array([12,45,67,89])
songs3[1]
##################################
import pandas as pd
songs3=pd.Series([14,12,38,13],name='George Songs',
                 index=[1900,1943,1900,1949])
songs3.index
print(songs3)
#########################
#CRUD (create, read , update and delete)

#read or access data and values
songs3[1949]
songs3[1900]
#using iterator
for i in songs3:
    print(i)
########################################

#update values in series
songs3[1949]=600
songs3[1949]
#################################################

#delete values in series
s=pd.Series([11,32,4,6],index=[1,2,3,4])
del s[1]
##############################################

#convert types
#string use .astypes(str)
#numeric use.astypes(int)
#it will fail for NaN values
#datetime use pd.to_datetime

songs_66=pd.Series([3,None,22,4],
                   index=['paul','John','George','Rango'],
                   name='counts')
pd.to_numeric(songs_66.astype(str))
#there will be error
pd.to_numeric(songs_66.astype(str),erroes='coerce')
#if we pass errors=coerce
#then we can see that it supports many formats

#dealing with none
songs_66.fillna(-1)
songs_66.dropna()
############################################################

#append combining and joining two series
import pandas as pd
songs_69=pd.Series([4,6,8,5],
                   index=['ram','sham','they','ayy'],
                   name='counts')
#to concatenate two series
songs=songs_66.append(songs_66)

#ploting two 
import matplotlib.pyplot as plt
fig=plt.figure()
songs_69.plot()
plt.legend()
############################################################

###################################################
fig=plt.figure()
songs_69.plot(kind='bar')
songs_69.plot(kind='bar',colour='b',alpha=.5)
plt.legend()
#####################################################

#numpy
import pandas as pd
import numpy as np
data=pd.Series(np.random.randn(500),
               name='500 random')
print(data)
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()
############################################

#NUMPY MODEL
import numpy as np
arr1=np.array([7,20,13])
arr2=np.array([3,5,2])
print(arr1)
print(arr2)
############################################

#mod()
mod_arr=np.mod(arr1,arr2) #[1 0 1]
print("after applying mod is:",mod_arr)
###########################################

#MULTIPLE ARRAY
arr=np.array([[10,20,30],[40,50,60]])
print(arr) 
#ndmin minimum diamensions
arr=np.array([10,20,30,40],ndmin=2) # 2D array
print(arr)
#################################################

arr=np.array([10,20,30,40],ndmin=3) # 3D array
print(arr)
####################################################
#change the datatype of array
arr=np.array([10,20,30,40],dtype=complex) # 3D array
print(arr.ndim) #to get the how D array is like 2D or 3D
print(arr)
###########################################

#find size of each item
arr=np.array([10,20,30]) #4 bytes
print("size",arr.itemsize) 
#############################################

#get the datatype of each item
arr=np.array([10,20,30]) #4 bytes
print("datatype of each item :",arr.dtype) 

#get shape size of array
arr=np.array([10,20,30])
print("size:",arr.size)   # 3
print("shape:",arr.shape) #3

#for multi diamentional array
arr=np.array([[10,20,30],[40,50,60]])
print("size:",arr.size)   # 6
print("shape:",arr.shape)  # (2,3)
############################################

#create numpy array from list
arr=np.array([[10,20,30],[40,50,60]])
print("array created from list:",arr)

#create a sequence of integer with arange()
#create for integer
#from 0 to 20 with 3 step
arr=np.arange(0,20,3)
print("sequential array with 3 step:",arr)
#############################################

#also using this same as range()
arr=np.arange(20)
print(arr)

#to get item  from array
print(arr[2]) #2
print(arr[-2]) #18
print(arr[6]) #6
print(arr[1,-1]) #for 2D array only
################################################

#using slicing
arr=np.arange(10)
print(arr)
x=arr[1:8:2] #[1,3,5,7]
print(x)
x=arr[-2:3:-1] #[]
print(x)

#indexing in numpy
import numpy as np
arr=np.array(
    [[10,20,10,40],
     [40,50,70,90],
     [60,10,70,80],
     [30,90,40,30]])

# 1 for column and 2 for column
x=arr[:3, ::2]
#all row and 3 column from arr1 
#all row and all column from arr2  and step of 2
print(x)
# output
#     [[10 10]
#     [40 70]
#     [60 70]]

#integer array indexing
arr=np.arange(35).reshape(5,7)
print(arr)

#boolean array indexing
import numpy as np
arr=np.arange(12).reshape(3,4)
print(arr)
rows=np.array([False,True,True])
wanted_rows=arr[rows ,:]
print(wanted_rows)
# output
#    [[ 4  5  6  7]
#     [ 8  9 10 11]]
#######################################################