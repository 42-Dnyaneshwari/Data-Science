# -*- coding: utf-8 -*-
"""
Created on Fri May 12 08:17:27 2023

@author: Dnyaneshwari....
"""
#spliting the input and output data
from numpy import array
#define array
data=array([11,22,33,44,55])
print(data[:-2])

from numpy import array
data=array([[11,22,33],
            [44,55,66],
            [77,88,99]])
#seperate data
x=data[:,:-1]
y=data[:,-1]
#data[:,-1]
# :   it takes all rows
# -1  keeps last column as it is
print(x)
print(y)
###################################################
from numpy import array
a=array([1,2,3])
print(a)
b=2
print(b)
c=a+b #b=2 is added in every element of array a and store it in c
print(c)
############################################
from numpy import array
from numpy.linalg import norm
#vector l1 norm
a=array([1,2,3,4])
print(a)
l1=norm(a,1)
print(l1)
#vector norm
a=array([5,3,7,6])
print(a)
#calculate norm
l2=norm(a)
print(l2)
##############################################
#triangular matrices
from numpy import array
from numpy import tril
from numpy import triu

#define sqare matrix
M=array([[1,2,3],
         [1,2,3],
         [1,2,3]])
print(M)
#lower triangular matrix
lower=tril(M)
print(lower)
#################################
#upper triangular matrix
upper=triu(M)
print(upper)
###################################
#diagonal matrix
import numpy as np
from numpy import diag
M=np.array([[1,2,3],
         [1,2,3],
         [1,2,3]
         ])
print(M)
#extract diagonal vector
d=diag(M)
print(d)
#create diagonal matrix from  vector
D=diag(d)
print(D)
#################################
#create a identity matrix
from numpy import identity
i=identity(3)
print(i)
##################################################
from numpy import array
from numpy.linalg import inv
q=array([[1,0],
         [0,-1]])
print(q)
v=inv(q)
print(q,v)
print(v)
########################################
#matplotlib used for bargraph
import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5])
plt.show()
#############################################
x=range(1,5)
plt.plot(x,[xi* 1.5 for xi in x])

plt.plot(x,[xi*3.0 for xi in x])

plt.plot(x,[xi/3.0 for xi in x])
plt.show()
#############################################
import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,5])
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)
plt.grid=True
plt.show()
######################################

import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,5])
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)
plt.axis([0,5,-1,13])
plt.show()
###############################################
#how to add lable in graph
import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5])
plt.xlabel('this is x axis')
plt.ylabel('this is y axis')
plt.show()
#############################################
#adding title
import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5])
plt.title('simple plot')
plt.show()
##########################################
#adding label as wel, as title
import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5])
plt.title('simple plot')
plt.xlabel('this is x axis')
plt.ylabel('this is y axis')
plt.show()
###########################################
#giving names to plots
import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,5])

plt.plot(x,x* 1.5 ,label='Normal')

plt.plot(x,x*3.0 ,label='Fast')

plt.plot(x,x/3.0 ,label='Slow')
plt.legend()
plt.show()
###############################################
#giving colurs
import matplotlib.pyplot as plt
import numpy as np
y=np.array([1,5])
plt.plot(y,'y')
plt.plot(y+1,'b')
plt.plot(y+2,'c')
plt.show()
##############################################
#changing colours
import matplotlib.pyplot as plt
import numpy as np
y=np.array([1,3])
plt.plot(y,'y',y+1,'b',y+2,'c');
plt.show()
####################################
#styles of line 1.solid line 2.dashed line3.slash dot line,dotted line
#changing style of graph
import matplotlib.pyplot as plt
import numpy as np
y=np.array([1,3])
plt.plot(y,'--',y+1,'-.',y+2,':');
plt.show()
##########################################
#marker of graph
import matplotlib.pyplot as plt
import numpy as np
y=np.array([1,3])
plt.plot(y,'*',y+1,'o',y+2,'D');
plt.show()
####################################################
#histogram
import matplotlib.pyplot as plt
import numpy as np


y=np.random.randn(1000)
plt.hist(y)
plt.show()
#################################
#bar graph called as univariable analysis
import matplotlib.pyplot as plt

#1 st list  cordinate or  pt at which yr bar has to be ploted
#2 nd list column height
plt.bar([1,2,3],[3,4,1]);
plt.show()
#########################################
#scatterd graph
import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y)
plt.show()
#######################################
#change colur of scatter graph
size=50*np.random.randn(1000)
colors=np.random.randn(1000)
plt.scatter(x,y,s=size,c=colors);
####################################################
#drow some text inside graph
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-4,4,1024)
y=.25*(x+4.)*(x+1.)*(x-2.)
plt.text(-0.5,-0.25,'helooooo')
plt.plot(x,y,c='b')
plt.show()
#############################################
