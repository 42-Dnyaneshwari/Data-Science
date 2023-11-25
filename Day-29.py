# -*- coding: utf-8 -*-
"""
Created on Wed May 31 08:21:27 2023

@author: Dnyaneshwari...
"""
'''
write a Numpy program to get the Numpy version 
and show the Numpy build configuration.
'''
import numpy as np 
print(np.__version__)
print(np.show_config())
#Write a NumPy program to get help with the add function. Import numpy as np #Write a NumPy program to test whether none of the elements of a given array are zero.
print(np.info(np.add))
#########################################################
import numpy as nр
x=np.array([1, 2, 3, 4]) 
print("Original array:")
print(x) 
print("Test if none of the elements of the said array is zero:")
print(np.all(x))
#output:True
############################################
x=np.array([0,1,2,3])
print("Orignal Array")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))#checking if all the elements are zero or not
#output:False
#####################################################
x=np.array([1,0,0,0,0])
print("Orignal Array")
print(x)
print("Test if none of the elements of the said array is nonzero:")
print(np.all(x))#checking if all the elements are nonzero or not
#output:False
########################################################
x=np.array([0,0,0,0,0])
print("Orignal Array")
print(x)
print("Test wether any of the elements of the said array is zero:")
print(np.any(x))#checking if any of the elements are zero or not
#output:False
##############################################################\
#to check given array element is finite or not
import numpy as np
x=np.array([0,1,np.nan,0,np.inf])
print("Orignal Array")
print(x)
print("Test wether any of the elements of the said array is zero:")
print(np.isfinite(x))#checking if all the elements are zero or not
#output:[ True  True False  True False]
################################################################
"""
Numpy Assignment
"""
"Write a numpy program to get numpy version "

import numpy as np
np._version_

np.show_config()

# Add function

np.info(np.add)

# transpose
# np.transpose

# test whether none of the element are zero giving True
x=np.array([1,2,3,4])

np.all(x)

# IF zero present giving False 
x=np.array([0,2,3,4])

np.all(x)

# Test any of element is non zero
x=np.array([0,0,23,0])
x
np.any(x)

# test for finite set
a=np.array([1,0,np.nan,np.inf])

np.isfinite(a)

# Check for complex number
a=np.array([1+2j,1+0j])
print(a)
print("Is number is complex : ")
np.iscomplex(a)
np.isreal(a)

np.isscalar(3.1)
np.isscalar([3.1])

a=[[11,12,12],[23,34,45],[23,34,54]]

# Show the dimenstion

A=np.array(a)
A

A.ndim

# Show shape
A.shape

# Row*Col
A.size

# Accesss rows and se
A[1,2]

A[1,2]

A[1,1]

A[0,0]

' OR '

A[0][0]

# 1st row and 1st and 2nd col

A[0][0:2]

A[:1,2]

# Basic operations 

x=np.array([[2,1],[2,4]])

y=np.array([[2,1],[2,4]])

# Add
Z=x+y
Z

# Sub
Z=x-y
Z

# Mul
Z=x*y
Z

"or "

Z=np.dot(x,y)
Z

# Calculate the sine of Z

np.sin(Z)

# Calucate transpose of matrix

c=np.array([[1,1],[2,2],[3,3]])
c

c.T
