# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 08:38:15 2023

@author: Dnyaneshwari...
"""
#image compression
#SVD
import numpy as np
from numpy import array
from scipy.linalg import svd

A=array([[1,0,0,0,2],
         [0,0,3,0,0],
         [0,0,0,0,0],
         [0,4,0,0,0]])
A

#SVD
u,d,Vt=svd(A)
print(u)
'''
array([[ 0.,  0.,  1.,  0.],
       [ 0.,  1.,  0.,  0.],
       [ 0.,  0.,  0., -1.],
       [ 1.,  0.,  0.,  0.]])
'''
print(d)
#[4.         3.         2.23606798 0.        ]
print(Vt)
'''
[[-0.          1.          0.         -0.          0.        ]
 [-0.          0.          1.         -0.          0.        ]
 [ 0.4472136  -0.         -0.         -0.          0.89442719]
 [ 0.          0.          0.          1.          0.        ]
 [-0.89442719  0.          0.          0.          0.4472136 ]]
'''
print(np.diag(d))
'''
[[4.         0.         0.         0.        ]
 [0.         3.         0.         0.        ]
 [0.         0.         2.23606798 0.        ]
'''
##################################################################

#svd applying to dataset
import pandas as pd
df=pd.read_csv("C:/Datasets/University_Clustering.csv")
df
df.describe()
df.columns
df=df.drop({'Expenses'},axis=1)
df.dtypes
df=df.iloc[:,2:]
df
##################################################################
from sklearn.decomposition import TruncatedSVD
svd=TruncatedSVD(n_components=3)
svd.fit(df)

res=pd.DataFrame(svd.transform(df))
res.columns='pc0','pc1','pc2'
res.head()

#scatter diagram
import matplotlib.pyplot as plt
plt.scatter(x=res.pc0,y=res.pc1)

