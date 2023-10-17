# -*- coding: utf-8 -*-
"""
Created on Thu May 11 08:17:23 2023

@author: Dnyaneshwari...
"""
#boolean array indexing
import numpy as np
arr=np.arange(12).reshape(3,4)
print(arr)
####################################

#########################################
rows=np.array([False,True,True])
wanted_rows=arr[rows ,:]
print(wanted_rows)
# output
#    [[ 4  5  6  7]
#     [ 8  9 10 11]]
##############################################

#convert numpy array to python list
#using tolist()
#################################################3
#convert 1D array to list
#create array
arr=np.array([10,20,30,40])
print("array :",arr)
print(type(arr))
#####################################################
#convert list
list=arr.tolist()
print("list:",list)
print(type(list))
################################################

#convert multi diamentional  array to list
arr=np.array(
    [[10,20,10,40],
     [40,50,70,90],
     [60,10,70,80],
     [30,90,40,30]])
print("array :",arr)
print(type(arr))
#convert list
lst=arr.tolist()
print("list:",lst)
print(type(lst))
##############################################

#convert a python list to a numpy array
#list can convert to array using 
# 1 numpy.array() 
# 2 numpy.asarray
# create list
lst=[20,30,40,60]

#convert array
#using np.array()
array=np.array(lst)
print(type(array))
#using np.asarray()
array=np.asarray(array)
print(type(array))
#########################################################

#numpy array properties
# 1 ndarray.size
# 2 ndarray.shape
# 3 ndarray.ndim
# 4 ndarray.itemsize
# 5 ndarray.dtype

######################################################
array=np.array([[10,20,30,40],[1,2,3,4]])
print(array)
print("size:",array.size)
print("shape:",array.shape)
print("datatype:",array.dtype)
print("itemsize:",array.itemsize)
print("how diamentional:",array.ndim)
###################################
#resize usage
array.shape=(4,2)
print(array)
##############################################
#reshape usage
new_array=array.reshape(2,4)
print(new_array)
################################################

#applying arithmatic opeartion on array
arr1=np.arange(16).reshape(4,4)
arr2=np.array([1,2,3,4])
#addition of two array sing n.add()
add_arr=np.add(arr1,arr2)
print("after add:\n",add_arr)
##########################################
#substract of two array usinh np.suntract()
sub_arr=np.subtract(arr1,arr2)
print("after sub:\n",sub_arr)
###############################################
#multiplication of two array using np.multiply
mul_arr=np.multiply(arr1,arr2)
print("after multiplication:\n",mul_arr)
####################################################
#division of two array using np.divide
div_arr=np.divide(arr1,arr2)
print("after multiplication:\n",div_arr)
#################################################

#resiprocal()
arr1=([50,10,3,5,1,200])
rep_arr=np.reciprocal(arr1)
print("after reciprocal of array output is:\n",rep_arr)

#np.power()
arr1=([3,10,5])
pow_arr=np.power(arr1,3)
print("after taking power of arr1:\n",pow_arr)
arr2=np.array([3,2,1])
pow_arr2=np.power(arr1,arr2)
print("after applying power of arr1 tp arr2 is:\n",pow_arr2)
#####################################################

#mod()
arr=([3,10,5])
mod_arr=np.mod(arr,10)
print("after applying mod:\n",mod_arr)
########################################################

#create an empty array
from numpy import array
l=[1,35,4,5]
a=array(l)
print(a)
#################################
from numpy import empty
l=[1,35,4,5]
a=empty(l)
print(a)
#############################################
#create zeros array
from numpy import zeros
a=zeros([3,5])
print(a)
###########################################
#create one array
from numpy import ones
a=ones([5])
print(a)
###################################################
#create v stack
from numpy import array
from numpy import vstack
#array 1
a1=array([1,3,5,4,5])
print(a1)
#array 2
a2=array([2,5,3,7,9])
print(a2)
#vertical stack
a3=vstack((a1,a2))
print(a3)
print(a3.shape)
##################################################
from numpy import array
from numpy import hstack
#array 1
a1=array([1,3,5,4,5])
print(a1)
#array 2
a2=array([2,5,3,7,9])
print(a2)
#horizontal stack
a3=hstack((a1,a2))
print(a3)
print(a3.shape)
######################################################
#access multi diamentional array
from numpy import array
data=array([[11,22],
       [33,44],
       [55,66]])
#index data
print(data[0,]) #zero the row and all column