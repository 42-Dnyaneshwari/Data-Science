# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 19:18:09 2024

@author: Dnyaneshwari
"""
'''
Independent var:Temperature
Dependnt var:Revenue
You have to build a DecisionTreeRegreesor
to study the relationnship b/w the two var of the icecream shop 
then predict the revenue of ice cream shop bases on temp and revenue

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor

#Import Dataset

df=pd.read_csv("C:/Decision Tree/IceCreamData.csv")
df.head(5)
df.tail(5)
df.describe()
df.shape
df.isnull().sum()
#0

#visualization

#scatterplot for analysis
plt.scatter(df['Temperature'],df['Revenue'])
plt.xlabel("Temperature")
plt.ylabel("Revenue")
plt.title("Scatter plot")


#heatmap for corelation
sns.heatmap(df.corr(),annot=True)

#WE Conclude the its very strong positive relations
#as the temp increase then revenue is also increases

#Boxplot for Outliers
plt.figure(figsize=(10, 10))
sns.boxplot(data=df)
plt.title('Boxplot of IceCreamData')
plt.xlabel('Temperature')
plt.ylabel('Revenue')
plt.show()

#Model Building

#Spliting of data
x=np.array(df.Temperature)
y=np.array(df.Revenue)

from sklearn.model_selection import train_test_split
#tain the data
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
len(X_train)

#choose the model
regressor=DecisionTreeRegressor()

#train the model
regressor.fit(X_train.reshape(-1,1),y_train.reshape(-1,1))

#testing the model

y_pred=regressor.predict(X_test.reshape(-1,1))
y_pred
#creating a new dataframe and comparing the values
comp=pd.DataFrame({"Actual Value":y_test.reshape(-1),
                   "Predicted Value":y_pred.reshape(-1)})
comp.head()

plt.scatter(y_test,y_test,color="red")
plt.scatter(y_pred,y_pred,color="green")
plt.xlabel("Temperature")
plt.ylabel("Revenue")
plt.title("Scatter plot")

sns.heatmap(comp.corr(),annot=True)

plt.figure(figsize=(10, 10))
sns.boxplot(data=comp)
plt.title('Boxplot of IceCreamData')
plt.xlabel('Temperature')
plt.ylabel('Revenue')
plt.show()

#Performance
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
r2_score(y_test,y_pred)
mean_squared_error(y_test, y_pred)
mean_absolute_error(y_test, y_pred)

#how to know right model is selected
#if the model's accuracy is compare with other model's accuracy



