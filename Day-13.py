# -*- coding: utf-8 -*-
"""
Created on Tue May  2 08:21:10 2023

@author: Nishant
"""
#checking version of packages 
import pandas as pd
pd.__version__
##########################################

##create pandas dataframe from list
import pandas as pd
tech=[
      ['Spark',20000,'30Days'],
      ['Pandas',2000,'40Days']
      ]
df=pd.DataFrame(tech)
print(df)
############################################
column_names=['Courses','Fees','Duration']
row_lable=['a','b']
df=pd.DataFrame(tech,columns=column_names,index=row_lable)
print(df)
##############################################

#checking datatypes of DataFrame using .dtypes
df.dtypes
###########################

#also assign custom datatypes to DataFrame
types={'Courses':str,'Fee':float,'Duration':str}
df.dtypes
################################################

#create DataFrame from dictionry
tech={
      'Courses':['python','java','spark'],
      'Fee':[1200,3400,4200],
      'Duration':["35_Days","45_Days",'55_Days']
      }
df=pd.DataFrame(tech)
print(df)
#############################################

#convert Dataframe to CSV file
df.to_csv("c:/1-Python/data_file2.csv")
######################################


#create DataFrame from csv file
df=pd.read_csv("c:/1-Python/data_file1.csv")
##############################################

#pandas basic opeartions
import pandas as pd
import numpy as np
tech=({
      'Courses':['python','java','spark',np.nan,'cpp'],
      'Fee':[1200,3400,4200,7800,None],
      'Duration':["35_Days","45_Days",'55_Days','66_Days','77_Days'],
      'Discount':[10,20,30,40,50]
      })
row_lables=['R0','R1','R2','R3','R4']
df=pd.DataFrame(tech,index=row_lables)
print(df)
#####################################################

#properties of dataframe
df.shape
df.size
df.columns
df.index
df.dtypes
#######################################################

#accessing one columns 
df['fee']
df[['fee','courses']]
############4###################################

#selecting row and assign it to the another DataFrame
#for 4 row and 1 column
df2=df[4:]
#for all row and 5 column
df3=df[:5]

#accessing certain cell from column fee
df['Fee'][3]

#
df['Fee'][3]-500
df['Fee']

#
df.describe()

###################################
df=pd.DataFrame(tech,index=row_lables)
df.columns={'A','B','C','D'}

df=pd.DataFrame(tech,index=row_lables)
df.columns={'A','C','D'}
df2=df.rename({'A':'C1','B':'C2'},axis=1)
df2=df.rename({'C':'C3','D':'C4'},axis='columns')
df2=df.rename(columns={'A':'C1','B':'C2'})
##############################################

#Assignment
################################################
#creatating a dict dataframe 
import pandas as pd
Dict={
      'Age':[10,11,12,13,14,15,16,17,18,19],
      'Default':[0,0,0,0,0,0,0,0,0,0],
      'Balance':[2143,29,2,1506,1,231,447,2,121,593],
      'Housing':[1,1,1,0,0,1,1,1,1,1],
      'Loan':[0,0,0,0,1,0,0,0,0,0]
      }
DD=pd.DataFrame(Dict)
print(DD)
#############################################
column_names=['C1','C2','C3','C4','C5']
row_lable=['R0','R1','R2','R3','R4','R5','R6','R7','R8','R9']
DD=pd.DataFrame(Dict,columns=column_names,index=row_lable)
print(DD)
#################################################

#DataFrame Properties
DD.shape    #(10,5)
DD.size     #50
DD.columns 
DD.index
DD.dtypes
####################################################

#Accessing one column content
DD['Age']
DD[['Age','Default']]
#######################################

#Select certain row and assign it to the another DataFrame
DD1=DD[5:]
#DD1 will select all the records starting from 5 to total size
DD2=DD[:5]
#DD2 will select all the records statring from 0 to 4
##############################################

#describe method
DD.describe()
################################################

#Rename()
DD=pd.DataFrame(Dict,index=row_lable)
DD.columns={'C1':'A','C2':'B','C3':'D','C4':'E','C5':'T'}
DD2=DD.rename({'C1':'A','C2':'B','C3':'D'},axis=1)
DD2=DD.rename({'C4':'V','C5':'K'},axis='columns')
DD2=DD.rename(columns={'C1':'A','C2':'B','C3':'D','C4':'E','C5':'T'})
#############################################################
