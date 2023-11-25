# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:19:51 2023

@author: Nishant
"""
# Boston.csv
import pandas as pd
import seaborn as sns
df=pd.read_csv("C:/1-Python/Boston.csv")
#eda,boxplot,oulier ndmin


#Exploratory Data Anlysis
df.describe()
df.columns
df.index
df.dtypes
df.shape


#1. TYPE CASTING
#using astype do type casting.
df.dtypes
#changing salaries of int to float
df.crim=df.crim.astype(int)
df.dtypes  


#2 FINDING DUPLICATES
#drop 
duplicates=df.duplicated()
duplicates
#output is a single column it present true otherwise false.
sum(duplicates)#0
# so no duplicates are present


#3. OUTLIERS ANALYSIS
sns.boxplot(df.crim)
sns.boxplot(df.age)
IQR=df.crim.quantile(0.75)-df.crim.quantile(0.25)
IQR
#3.0

lower_limit=df.crim.quantile(0.75) - 1.5*IQR
lower_limit
#-1.5
upper_limit=df.crim.quantile(0.75) + 1.5*IQR
upper_limit
#7.5

# OUTLIER TREATMENT

#TRIMMING

import numpy as np
outliers_df=np.where(df.crim > upper_limit,True, np.where(df.crim<lower_limit,True,False)) 
outliers_df
df_trimmed=df.loc[~ outliers_df]
df_trimmed
df.shape
#(506, 15)
df_trimmed.shape
#(430, 15)
#therefore there are 76 outliers that is trimmed


#REPLACEMENT TECHQUIES
df_replaced=pd.DataFrame(np.where(df.crim > upper_limit , upper_limit,np.where(df.crim < lower_limit , lower_limit,df.crim)))
#if values are greter than upper limit mapped to the upper limit
#if values are lower than lower limit mapped to the lower limit

sns.boxplot(df_replaced[0])



#Winsorizer
from feature_engine.outliers import Winsorizer

winsor=Winsorizer(capping_method='iqr',
                  tail='both',
                  fold=1.5,
                  variables=['crim'])

df_t=winsor.fit_transform(df[{'crim'}])
sns.boxplot(df['crim'])
sns.boxplot(df_t['crim'])
#################################################################




import pandas as pd
import seaborn as sns
df=pd.read_csv("C:/1-Python/Onlineretail.csv")
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa3 
#in position 79780: invalid start byte
df.describe()
################################################################