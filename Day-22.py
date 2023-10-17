# -*- coding: utf-8 -*-
"""
Created on Sat May 13 08:20:16 2023

@author: Dnyaneshwari...
"""
#seaborn 
#pip install seabborn
import seaborn as sns
import pandas
import matplotlib.pyplot as plt
import pandas as pd
sns.get_dataset_names()
df=sns.load_dataset('titanic')
df.head()
#count plot
import seaborn as sns
import pandas as pd
df=pd.read_csv('C:/1-Python/Titanic-Dataset.csv')
sns.countplot(x='Sex',data=df)
#over python for data science
#data=dataframe
#hue=category
sns.countplot(x='Sex',hue='Survived',data=df,
palette='Set1')

sns.countplot(x='Sex',hue='Survived',data=df,
palette='Set2')

sns.countplot(x='Sex',hue='Survived',data=df,
palette='Set3')
################################################
sns.kdeplot(x='Age',data=df,c='black')
#x name of column
#c colour of graph
plt.hist(df.Age)

##################################################
#distribution plot
sns.displot(x='Age',kde=True,bins=5,data=df)
sns.displot(x='Age',kde=True,bins=5,
            hue=df['Survived'],palatte='Set1',data=df)
#########################
import seaborn as sns
import pandas as pd
df=pd.read_csv('IRIS.csv')
#######################################
#histogram
plt.hist(df.sepal_length)
plt.hist(df.sepal_width)
plt.hist(df.petal_length)
plt.hist(df.petal_width)
#bar graph
plt.bar(df['sepal_length']);
plt.show()
#####################################
#used to plot the co-relation
sns.jointplot(x='sepal_length',y='petal_length',
                data=df,kind='reg')
##############################################
sns.countplot(x='sepal_length',data=df,
palette='Set1')
####################
#bivarient analysis
sns.scatterplot(x='sepal_length',y='petal_length',data=df,
palette='Set1')
#pair plot
sns.pairplot(df)
#heatmap
corr=df.corr()
sns.heatmap(corr)
#########################################
#df=sns.load_dataset('iris')
#df.head()
sns.scatterplot(x='sepal_length',y='petal_length',
                data=df,hue='species')
############################################
#used to plot the co-relation
sns.jointplot(x='sepal_length',y='petal_length',
                data=df,kind='reg')

sns.jointplot(x='sepal_length',y='petal_length',
                data=df,kind='hist')

sns.jointplot(x='sepal_length',y='petal_length',
                data=df,kind='kde')
#pair plot
sns.pairplot(df)
###########################################
#a heat map can be used for visualising ,confusion
#matrices
corr=df.corr()
sns.heatmap(corr)
###################################################
from scipy.stats import skew
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
cars=pd.read_csv('C:/1-Python/Q1_a.csv')
cars.columns
cars.describe()

plt.hist(cars.speed)
sns.displot(x='speed',kde=True,bins=6,)
sns.displot(x='dist',kde=True)
cars.describe()
#speed datails left skewed
sns.boxplot(cars.speed)
#means speed of all cars
plt.hist(cars.dist)
#dist datails right skewed
sns.boxplot(cars.speed)
#there is one outlayer
speed=cars['speed'].tolist()
speed
print("skewness of speed",skew(speed))
dist=cars['dist'].tolist()
dist
print("skewness of speed",skew(dist))
#########################################
print(skew(dist,axis=0,bias=True))
#print(kurtosis(dist,axis=0,bias=True))
#cars ke liye bar,joint,heatmap draw
#bar graph
plt.bar(cars[speed]);
plt.show()
#####################################
#used to plot the co-relation
sns.jointplot(x='speed',y='dist',
                data=cars,kind='reg')
##############################################
sns.countplot(x='speed',data=cars,
palette='Set1')
####################
sns.scatterplot(x='speed',y='dist',data=cars,
palette='Set1')
#pair plot
sns.pairplot(cars)
#heatmap
corr=cars.corr()
sns.heatmap(corr)
#assignmnet
#write datadictonary of iris dataset
#create dataframe
#df.columns
import seaborn as sns
import pandas as pd
df=pd.read_csv('IRIS.csv')
#######################################
#histogram
plt.hist(df.sepal_length)
plt.hist(df.sepal_width)
plt.hist(df.petal_length)
plt.hist(df.petal_width)
#bar graph
plt.bar(df);
plt.show()
#####################################
#used to plot the co-relation
sns.jointplot(x='sepal_length',y='petal_length',
                data=df,kind='reg')
##############################################
#count is same as bar graph
sns.countplot(x='sepal_length',data=df,
palette='Set1')
####################
sns.scatterplot(x='sepal_length',y='petal_length',data=df,
palette='Set1')
#pair plot
sns.pairplot(df)
#heatmap
corr=df.corr()
sns.heatmap(corr)
#################################################