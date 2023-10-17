# -*- coding: utf-8 -*-
"""
Created on Tue May  9 08:23:54 2023

@author: Dnyaneshwari...
"""

import pandas as pd
import numpy as np
tech={
      'Courses':['Spark','Pyspark','Python','Pandas'],
        "Fee":[20000,30000,40000,50000],
        'Duration':['3odays','40days','50days','20days']
      }
index_lables=['r1','r2','r3','r4']
df1=pd.DataFrame(tech,index=index_lables)

tech2={
       'Courses':['Spark','Java','Python','Go'],
       'Discount':[200,300,400,500]
       }
index_lables2=['r1','r6','r3','r5']
df2=pd.DataFrame(tech2,index=index_lables2)

#while joining if we do not mension the column name then 
#matching is done by index
#pandas join by default it will join the table left join

df3=df1.join(df2,lsuffix='_left',rsuffix='_right')
print(df3)
#########################################################

#pandas right join dataframe
df3=df1.join(df2,lsuffix='_left',rsuffix='_right',how='right')
print(df3)
#####################################################

#pandas inner join dataframe
df3=df1.join(df2,lsuffix='_left',rsuffix='_right',how='inner')
print(df3)
#####################################################

#pandas full outer join dataframe
#use outer
df3=df1.join(df2,lsuffix='_left',rsuffix='_right',how='outer')
print(df3)
############################################################

#pandas join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses') ,how='inner')
print(df3)
##########################################################

#pandas merge DataFrame
import pandas as pd
import numpy as np
tech={
      'Courses':['Spark','Pyspark','Python','Pandas'],
        "Fee":[20000,30000,40000,50000],
        'Duration':['3odays','40days','50days','20days']
      }
index_lables=['r1','r2','r3','r4']
df1=pd.DataFrame(tech,index=index_lables)

tech2={
       'Courses':['Spark','Java','Python','Go'],
       'Discount':[200,300,400,500]
       }
index_lables2=['r1','r6','r3','r5']
df2=pd.DataFrame(tech2,index=index_lables2)
###################################################


#using pandas.merge()
df3=pd.merge(df1,df2)
################################################

#Using DataFrame.merge()
df3.merge(df2)
##############################################################################
#use pandas.concat() to connect two dataframes

import pandas as pd
df=pd.DataFrame({
    'courses':["spark","pandas","Pyspark","Hadoop","python"],
    'Fee':[10000,30000,20000,30000,40000,],
   
    })
df1=pd.DataFrame({
    'courses':["spark","pandas","Pyspark","Hadoop","python"],
    'Fee':[1789,3067,20000,30000,4456],
   
    })
df2=pd.DataFrame ({ 
    'Duration':['1days','4days','2days','3days','4days'],
 'Discount':[1.1,1.6,1.2,1.3,1.4] } )

#using pandas.concat() to concat two dataframes
data=[df,df1]
df2=pd.concat(data)
df2
#################################################################
#Concatinate multiple DataFrames
df3=pd.concat[( df,df1,df2)]
print( df3)

#Write dataframe to csv file with default [parameters
df3.to_csv(" c:/1-python/courses.csv")
#read CSV
#Import pandas
import pandas as pd
#Read CSV file into DataFrame
df=pd.read_csv( 'courses.csv')
print( df)

#Write dataFrames to excel file
df.to_excel(' c:/1-python/courses.xlsx')


#######################@@@@@@@@@@@@@@@@@@@@@@@@@#########################
#Series
 #It is used to model one dimentional data
#similar to list in pyhton
#the series object alsio has a few more bits
#of data including name and index

import pandas as pd
song2=pd.series([145,142,38,13])
#It is easy to inspect the index of a series or data frame
song2.index
#The data can be string based as well