# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 08:32:52 2023

@author: Dnyaneshwari...
"""
import numpy as np
a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
print("Original array")
print(a)
#[1. +1.j 1. +0.j 4.5+0.j 3. +0.j 2. +0.j 0. +2.j]
print("Checking for complex number:")
print(np.iscomplex(a))
#[ True False False False False  True]
###################################################
print("Checking for real number:")
print (np.isreal(a))
#[False  True  True  True  True False]
###################################################
print("Checking for scalar type:")
print (np.isscalar(3.1))
#True
print(np.isscalar([3.1]))
#False
#########################################################
#dot product or matrix multiplication
import numpy as np
p = [[1, 0], [0, 1]]
q=[[1, 2], [3, 4]]

print("original matrix:")
print(p)
#[[1, 0], [0, 1]]
print(q)
#[[1, 2], [3, 4]]
result1=np.dot(p, q)
print("Result of the said matrix multiplication:")
print(result1)
# [[1 2]
#[3 4]]
###############################################################

#Write a NumPy program to compute the outer product
# of two given vector
import numpy as np

p = [[1, 0], [0, 1]] 
q= [[1, 2], [3, 4]]

print("original matrix:")
print(p)
#[[1, 0], [0, 1]] 
print(q)
#[[1, 2], [3, 4]]
result = np.outer(p, q) 
print("Outer product of the said two vectors: ")
print(result)
'''
output:
    [[1 2 3 4]
     [0 0 0 0]
     [0 0 0 0]
     [1 2 3 4]]
'''
######################################################################
#cross product of two vectors
import numpy as np

p = [[1, 0], [0, 1]] 
q= [[1, 2], [3, 4]]

print("original matrix:")
print(p)
#[[1, 0], [0, 1]] 
print(q)
#[[1, 2], [3, 4]]
result1 = np.cross(p, q) 
result2 = np.cross(q,p) 
print("cross product of  two vectors: ")
print(result1)
#[ 2 -3]
print(result2)
#[-2  3]
#####################################################################
#finding a determinant of a square matrix
import numpy as np
from numpy import linalg as LA
# creating a 2X2 Numpy matrix
a= np.array([[1,0], [1,2]])
  
# Displaying the Matrix
print("Numpy Matrix is:")
print(a)
  
# calculating the determinant of matrix
det = np.linalg.det(a)
  
print("\nDeterminant of given 2X2 matrix:")
print(int(det))
#2
#########################################################
#to calculate eigen values and eigen vectors
import numpy as np
  
# create numpy 2d-array
m = np.mat("3 -2;1 0")
  
print("Printing the Original square array:\n",
      m)
#[[1 2]
#[2 3]]

# finding eigenvalues and eigenvectors
w, v = np.linalg.eig(m)

# printing eigen values
print("Printing the Eigen vector of the given square array:\n",w)
# [2. 1.]

# printing eigen vectors
print("Printing Right eigen values of the given square array:\n",v)
#[[0.89442719 0.70710678]
#[0.4472136  0.70710678]]
#######################################################################
#finding inverse of matrix
# Import required package
import numpy as np

# Taking a 3 * 3 matrix
A = np.array([[1,2],
			[3,4]])

# Calculating the inverse of the matrix
print("inverse of matrix A is:",np.linalg.inv(A))
#[[-2.   1. ]
#[ 1.5 -0.5]]
############################################################

#genrate 5 random numbers from normal distribution

import numpy as np
# numpy.random.normal() method
random_array = np.random.normal(size=15)

# printing 1D array with random numbers
print("1D Array with random values : \n", random_array)
'''
output:
    [ 0.10674735  0.70182121 -0.4382541   
     0.05471335 -0.75642742  0.56219805
    -0.10738297  1.78341605  2.63530136 
     2.13098943 -0.52414906  0.71048191
     0.28012803 -0.79262419 -1.75702068]
'''
####################################################################

#genrate 6 random int numbers from  1 to 16
import random
print(np.random.randint(10,30,6))
#[14 21 25 27 13 18]
####################################################################

#create 3x3 array with random values
x=np.random.random((3,3,3))
print(x)
'''
output:
        [[[0.92218887 0.96120954 0.72703988]
          [0.60751275 0.36269233 0.02929453]
          [0.84219598 0.03289182 0.8399016 ]]

         [[0.49926116 0.30957547 0.25832699]
          [0.77204234 0.91627979 0.9378325 ]
          [0.01854828 0.63186532 0.38648064]]

         [[0.6014977  0.73209595 0.011025  ]
          [0.82079643 0.27146572 0.73715911]
          [0.15836907 0.37925515 0.24765618]]]
    
    '''
##################################################
#create 5x5 matrix with min and maz vaules
x=np.random.random((5,5,5))
print(x)
'''
output:
[[[8.83740680e-01 3.61338477e-01 8.22103001e-01 3.40601813e-01
   1.49919168e-01]
  [5.71516891e-01 2.55439852e-01 9.76546352e-01 7.65687209e-01
   2.68362099e-01]
  [1.38307420e-01 5.21046605e-02 8.98311422e-01 3.73278120e-01
   6.86578839e-01]
  [4.29911945e-01 1.29258502e-01 6.69786939e-01 5.15878762e-01
   9.85164542e-01]
  [2.32179934e-01 5.44312318e-01 6.04249135e-01 6.51247550e-01
   7.93548685e-01]]

 [[6.53634309e-02 2.52858543e-01 2.91944215e-01 8.56433206e-01
   1.40178228e-01]
  [6.64948372e-01 6.87289430e-01 8.15186069e-01 6.01434124e-01
   8.44211205e-01]
  [8.17045623e-01 8.96744860e-01 7.87543954e-01 2.09850533e-01
   2.32950789e-01]
  [3.59316433e-01 5.33091397e-01 6.71720297e-01 6.36051675e-01
   9.23361848e-01]
  [1.42401554e-01 3.88009266e-01 5.32669747e-02 6.07883846e-01
   9.23913379e-01]]

 [[2.57275925e-01 6.38097050e-01 8.33848535e-01 1.02073523e-01
   7.09590512e-01]
  [3.53752722e-01 1.24755987e-01 8.96869244e-04 8.68732800e-01
   6.18207376e-01]
  [1.23194471e-01 8.69913511e-01 4.41558365e-01 6.73556328e-01
   3.36584060e-01]
  [6.26938800e-01 1.90029322e-01 5.68259607e-01 1.12382379e-01
   5.57101376e-01]
  [2.40447545e-01 9.23895571e-01 9.16648464e-01 2.07196432e-01
   8.52198574e-02]]

 [[6.85285183e-01 3.85320871e-01 8.30768992e-01 5.10418953e-01
   1.25807102e-01]
  [8.24505450e-02 6.66628730e-01 3.09880473e-01 9.83519237e-01
   6.79013538e-01]
  [9.12170914e-01 5.00649994e-01 2.51677256e-01 4.22596904e-01
   8.31559887e-01]
  [2.94141117e-01 9.69982730e-01 6.05693416e-02 4.81218296e-01
   7.32834616e-01]
  [1.04927064e-02 3.15547280e-01 4.53927083e-01 7.67350195e-01
   1.53468956e-01]]

 [[9.78845749e-01 4.07974880e-02 3.44536722e-01 3.00263205e-01
   3.88522171e-01]
  [3.69066857e-01 3.66023724e-01 9.01946838e-02 2.34321385e-01
   7.77336474e-01]
  [5.54636969e-01 6.04082359e-01 5.15047156e-01 3.27167445e-01
   6.96084998e-01]
  [7.20611776e-01 3.03460818e-01 3.84064948e-01 1.02229710e-01
   6.57192166e-01]
  [7.92856224e-01 8.25211742e-01 5.98694623e-01 3.77489455e-01
   2.49281159e-01]]]
'''
xmin,xmax=x.min(),x.max()

print("Minimum values and Maximum Values")
print(xmin,xmax)
#0.0008968692441975179 ,0.9851645418831022
##########################################################################
