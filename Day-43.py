# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 08:27:21 2023

@author: Dnyaneshwari
"""

import pandas as pd
import seaborn as sns
df=pd.read_csv("C:/1-Python/animal_category.csv")
df
#eda,boxplot,oulier ndmin

#Exploratory Data Anlysis
df.describe()
df.columns
df.index
df.dtypes
df.shape

import pandas as pd
data=pd.read_csv("modifiedethnic.csv")
data.head(10)
data.info
data.describe()
data['Salaries_new']=pd.cut(data['Salaries'],
        bins=[min(data.Salaries),data.salaries.mean(),
         max(data.Salaries)],lables=["low","high"])
data.Salaries_new.value_counts()
data['Salaries_new']=pd.cut(data['Salaries'],
        bins=[min(data.Salaries),data.salaries.quantile(0.25),
              data.salaries.mean(),data.salaries.quantile(0.7),
         max(data.Salaries)],lables=["group1","group1","group3","group4"])


####################################################################
#create dummy 


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df3 = pd.read_csv('C:/2-dataset/animal_category.csv')
df3.shape
df3.columns
df3.drop(['Index'],axis =1,inplace=True)
df_new = pd.get_dummies(df3)
df_new.shape
#here we are getting 30 rows ad 14 cols
#we are getting two cols for homly and gender and one col for 
#delete second col of gender and second column of homely
df_new.drop(['Gender_Male','Homly_Yes'],axis=1,inplace=True)
df_new.shape

df_n=df_new.rename(columns={'Gender_Female':'Gender','Homly_No':'Homly'})
df_new


#**************************************************************************
#dummy var on ethnic diversity

df.shape
df.columns
df.drop('Employee_Name',axis=1,inplace=True)
df_d=pd.get_dummies(df3)
df_d.shape
df_d.columns


####################################################################


import pandas as pd
from sklearn.preprocessing import OneHotEncoder
df=pd.read_csv("C:/1-Python/modifies_diversity.csv")
df
df.columns
enc=OneHotEncoder()
df=df[['Salaries','age','Position','State','Sex','MaritalDesc','CitizenDesc','EmploymentStatus', 'Department','Race']]
enc_df=pd.DataFrame(enc.fit_transform(df.iloc[:,2:]).toarray())
enc_df


#################################################################
#label encoder
#labelenoding is done only nomaailnal data not ordinal data


from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
X=df.iloc[:,0:9]
y=df['Race']
df.columns
#we have nominal data  Sex, CitizenDesc, MaritalDesc
#we want to conver it into label encoderSS
X['Sex']=labelencoder.fit_transform(X['Sex'])
X['CitizenDesc']=labelencoder.fit_transform(X['CitizenDesc'])
X['MaritalDesc']=labelencoder.fit_transform(X['MaritalDesc'])
y=labelencoder.fit_transform(y)
y=pd.DataFrame(y)
y
df_new=pd.concat([X,y],axis=1)
df_new=df_new.rename(columns={0:'Race'})
df_new


##########################################################################                                                                        
  

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
d=pd.read_csv("C:/1-Python/mtcars_dup.csv")
d
a=d.describe()                                                                                        
a
#innitialise the scaler
scaler=StandardScaler()
df=scaler.fit_transform(df)
dataset1=pd.DataFrame(df)
dataset1
res=dataset1.describe()
res


##################################################################


from sklearn.preprocessing import StandardScaler 
import pandas as pd

df=pd.read_csv("C:/1-Python/mtcars.csv")

df.head()

a=df.describe()
a
scaler=StandardScaler()
scaler
df=scaler.fit_transform(df) 
dataset2=pd.DataFrame(df)
dataset2
res=dataset2.describe()
res


#################################################################


from sklearn.preprocessing import StandardScaler
import pandas as pd 
df=pd.read_csv("C:/1-Python/seeds.csv")
df.head()
a=df.describe()
a
scaler=StandardScaler()
scaler
df=scaler.fit_transform(df) 
dataset3=pd.DataFrame(df)
dataset3
res=dataset3.describe()
res

#####################################################################