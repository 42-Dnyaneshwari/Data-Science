# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 09:39:37 2023

@author: Nishant
"""
#perform all EDA operations
import pandas as pd
df=pd.read_csv("C:/1-Python/ethnic diversity.csv")
df

#1. TYPE CASTING
#using astype do type casting.
df.dtypes
#changing salaries of int to float
df.Salaries=df.Salaries.astype(int)
df.dtypes


#changing age int to float
df.age=df.age.astype(float)
df.dtypes
#################################################################
#2 FINDING DUPLICATES
#drop 
import pandas as pd
df_new=pd.read_csv("C:/1-Python/education.csv")
df_new
duplicates=df_new.duplicated()
duplicates
#output is a single column it present true otherwise false.
sum(duplicates)#0
# so no duplicates are present


#drop_dupliacates(): drop duplicate records
import pandas as pd
df_new=pd.read_csv("C:/1-Python/mtcars_dup.csv")
df_new
duplicates=df_new.duplicated()
duplicates
sum(duplicates)
df_new.drop_duplicates()
duplicates
###########################################################################

#3. OUTLIERS ANALYSIS
'''

3 R rule :- ( Rectify , Retain , Remove )
Trimming removal
Winsorization rounding up

'''

import pandas as pd
import seaborn as sns
df=pd.read_csv("C:/1-Python/ethnic diversity.csv")
df


sns.boxplot(df.Salaries)
sns.boxplot(df.age)
IQR=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
IQR
#28359.945


lower_limit=df.Salaries.quantile(0.75) - 1.5*IQR
lower_limit
#8912.9775
upper_limit=df.Salaries.quantile(0.75) + 1.5*IQR
upper_limit
#93992.8125

#########################################################################
# OUTLIER TREATMENT

#TRIMMING

import numpy as np
outliers_df=np.where(df.Salaries > upper_limit,True, np.where(df.Salaries<lower_limit,True,False)) 
outliers_df
df_trimmed=df.loc[~ outliers_df]
df_trimmed
df.shape
#(310, 13)
df_trimmed.shape
#(306, 13)

##################################################################

#REPLACEMENT TECHQUIES

import pandas as pd
import seaborn as sns
df=pd.read_csv("C:/1-Python/ethnic diversity.csv")
df.describe()
df_replaced=pd.DataFrame(np.where(df.Salaries > upper_limit , upper_limit,np.where(df.Salaries < lower_limit , lower_limit,df.Salaries)))
#if values are greter than upper limit mapped to the upper limit
#if values are lower than lower limit mapped to the lower limit

sns.boxplot(df_replaced[0])
#######################################################
