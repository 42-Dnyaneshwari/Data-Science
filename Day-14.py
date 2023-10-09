# -*- coding: utf-8 -*-
"""
Created on Wed May  3 08:17:06 2023

@author: Nishant
"""

import pandas as pd
DD=pd.read_csv('C:/1-Python/Company_Data.csv.xls')
print(DD)
DD.dtypes
#DataFrame Properties
DD.shape    #(10,5)
DD.size     #50
DD.columns 
DD.index
DD.dtypes
####################################################

#Accessing one column content
DD['Sales']
DD[['Sales','CompPrice']]
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
DD=pd.DataFrame(tech,index=row_lable)
DD.columns={'C1':'A','C2':'B','C3':'D','C4':'E','C5':'T'}
DD2=DD.rename({'C1':'A','C2':'B','C3':'D'},axis=1)
DD2=DD.rename({'C4':'V','C5':'K'},axis='columns')
DD2=DD.rename(columns={'C1':'A','C2':'B','C3':'D','C4':'E','C5':'T'})
#############################################################

#Drop row
#drop by lable
DD1=DD.drop([['R0','R2']])
#################################################

#drop by index or position
DD1=DD.drop(DD.index[[1,3]])
##########################################

#Delete row by index range
DD1=DD.drop(DD.index[2:])
#########################################

#when u have default index then 
#how to delete a row
DD=pd.DataFrame(tech)
DD1=DD.drop(0)
#######################################
DD=pd.DataFrame(tech)
#############################################
DD1=DD.drop([1,2])
#############################################
DD1=DD.drop(range(0,2))
###########################################


###############################################
#drop column
DD=pd.read_csv('C:/1-Python/Company_Data.csv.xls')
print(DD)

#drop column by name
DD1=DD.drop(['Sales'],axis=1) #drop customer
print(DD1)

#drop column by lable explicitly
DD2=DD.drop(labels=['Sales'],axis=1) #drop customer
print(DD)
DD2=DD.drop(labels=['CompPrice'],axis=1) #drop response
print(DD)
#####################################################
#using inplace=true
DD=pd.DataFrame(tech)

DD.drop(DD.columns[[1]],axis=1,inplace=True)
#################################################
import pandas as pd
#drop 2 or more column by lable name
DD2=DD.drop(['Sales','CompPrice'],axis=1)
print(DD2)
############################################

#
DD2=DD.drop(DD.columns[[0,1]],axis=1)
print(DD2)
#############################################

#drop a column from  list of column
#DD=pd.DataFrame(tech)
lst=['Sales','CompPrice']
DD2=DD.drop(lst,axis=1)
print(DD2)
##########################################

#remove column from dataframe inplace
DD.drop(DD.columns[1],axis=1,inplace=True)
DD
################################################


#ASSIGNMENT 2
import pandas as pd
import numpy as np
tech=(
      {
      'Customer':['BU79786','QZ44356',None,'WW63253','HB64268','OC83172','XZ87318','CF85061','DY87989','BQ94931'],
      'State':['Washington','Arizona','Nevada','California','Washington','Oregon','Oregon','Arizona',None,'Oregon'],
      'Response':['No','No',None,'No','No','No','No','No','No','No'],
      'Education':['Bachelor','Bachelor','Bachelor','Bachelor','Bachelor','Bachelor','College','Master','Bachelor','College'],
      'Income':[123.00,343.00,432.00,728.00,None,821.88,923.0,123.98,234.09,456.90]
      }
      )
DD=pd.DataFrame(tech)
print(DD)
DD.dtypes
print(DD.dtypes)
####################################


DD=pd.DataFrame(tech)
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
DD['Customer']
DD[['Customer','State']]
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
DD=pd.DataFrame(tech,index=row_lable)
DD.columns={'C1':'A','C2':'B','C3':'D','C4':'E','C5':'T'}
DD2=DD.rename({'C1':'A','C2':'B','C3':'D'},axis=1)
DD2=DD.rename({'C4':'V','C5':'K'},axis='columns')
DD2=DD.rename(columns={'C1':'A','C2':'B','C3':'D','C4':'E','C5':'T'})
#############################################################

#Drop row
#drop by lable
DD1=DD.drop([['R0','R2']])
#################################################

#drop by index or position
DD1=DD.drop(DD.index[[1,3]])
##########################################

#Delete row by index range
DD1=DD.drop(DD.index[2:])
#########################################

#when u have default index then 
#how to delete a row
DD=pd.DataFrame(tech)
DD1=DD.drop(0)
#######################################
DD=pd.DataFrame(tech)
#############################################
DD1=DD.drop([1,2])
#############################################
DD1=DD.drop(range(0,2))
###########################################


###############################################
#drop column
DD=pd.DataFrame(tech)
print(DD)

#drop column by name
DD1=DD.drop(['Customer'],axis=1) #drop customer
print(DD1)

#drop column by lable explicitly
DD2=DD.drop(labels=['Customer'],axis=1) #drop customer
print(DD)
DD2=DD.drop(labels=['Response'],axis=1) #drop response
print(DD)
#####################################################