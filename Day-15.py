# -*- coding: utf-8 -*-
"""
Created on Thu May  4 08:12:38 2023

@author: Dnyaneshwari...
"""

#drop column
import pandas as pd
import numpy as np
tech=(
      {
      'Courses':['python','java','spark',np.nan,'cpp','hello','dotnet'],
      'Fee':[12.00,34.00,42.00,78.00,None,8.88,9.0],
      'Duration':["35_Days","45_Days",'55_Days','66_Days','77_Days','44_Days','33_Days'],
      'Discount':[10,20,30,40,50,60,70]
      }
      )
row_lables=['R0','R1','R2','R3','R4','R5','R6']
DD=pd.DataFrame(tech,index=row_lables)
print(DD)
DD=pd.DataFrame(tech)
print(DD)

#drop column by name
DD1=DD.drop(['Fee'],axis=1)
print(DD1)

#drop column by lable explicitly
DD2=DD.drop(labels=['Fee'],axis=1)
print(DD)
#####################################################

#alternatively you can also use columns instead of lables
DD2=DD.drop(columns=['Fee'],axis=1)

#drop column by its index\
print(DD.drop(DD.columns[[1]],axis=1))

#using inplace=true
DD=pd.DataFrame(tech)

DD.drop(DD.columns[[1]],axis=1,inplace=True)
#################################################

#drop 2 or more column by lable name
DD=pd.DataFrame(tech)
DD2=DD.drop(['Courses','Duration'],axis=1)
print(DD2)
############################################

######################################
DD2=DD.drop(DD.columns[[0,1]],axis=1)
print(DD2)
#############################################

#drop a column from  list of column
DD=pd.DataFrame(tech)
lst=['Courses','Fee']
DD2=DD.drop(lst,axis=1)
print(DD2)
##########################################

#remove column from dataframe inplace
DD.drop(DD.columns[1],axis=1,inplace=True)
DD
################################################

#pandas select rows by index position / lable
import pandas as pd
import numpy as np
tech=({
      'Courses':['python','java','spark',np.nan,'cpp'],
      'Fee':[1200,3400,4200,7800,None],
      'Duration':["35_Days","45_Days",'55_Days','66_Days','77_Days'],
      'Discount':[10,20,30,40,50]
      })
row_lables=['R0','R1','R2','R3','R4']
DD=pd.DataFrame(tech,index=row_lables)
print(DD)

#using iloc  
#syntac
#DD.iloc[startindex : endindex , startcolumn : endcolumn]
#example
DD=pd.DataFrame(tech,index=row_lables)
DD2=DD.iloc[:,0:2] #select all row and 2 i.e.(0,1) column
#this line uses the slicing operator to get DataFrame
DD2
##################################################

DD2=DD.iloc[0:2,:] #selct 2 row i.e.(0,1) and all columns
DD2

#both
DD2=DD.iloc[0:2,0:2]
DD2
DD2=DD.iloc[:,1:3] #select all row and (1,2) column
########################################################

#selct row using index 
DD2=DD.iloc[2]
DD2

DD2=DD.iloc[[1,2,3]]#select row by index list
DD2=DD.iloc[1:5] #select row 1,2,3,4
DD2=DD.iloc[:1] #select row first
DD2=DD.iloc[:3] #select row 0,1,2
DD2=DD.iloc[-1:] #select row last
DD2=DD.iloc[-3:] #select row 3 last
DD2=DD.iloc[::2] #select alternate row 
##################################################3

#loc
#select row by index lable
DD2=DD.loc['R2'] #select row 2
DD2=DD.loc[['R0','R1','R3']] #select row 2,3,4
DD2=DD.loc['R1':'R3'] #select row 1,2
DD2=DD.loc['R1':'R5':2] #
DD2
###################################################

#pandas select column using names
DD2=DD['Fee']

DD2=DD[['Fee','Courses','Duration']]

#loc to slice 
#DD.loc[:,start:stop:step]
#select multiple columns
DD2=DD.loc[:,['Courses','Fee']]
#select random column
DD2=DD.loc[:,['Courses','Fee','Duration']]
#select column by range
DD2=DD.loc[:,'Courses','Fee']
#select column between two columns
DD2=DD.loc[:,'Fee':'Duration']
#all the column upto Duration
DD2=DD.loc[:,'Duration':]
#before duration all column will be selected
DD2=DD.loc[:,:'Duration']
############################################
#query all row with courses equal to spark
#pandas dataframe.query()
#equal conditions
DD2=DD.query("Courses=='spark'")
print(DD2)

#not equal conditions
DD2=DD.query("Courses != 'spark'")
print(DD2)


import pandas as pd
import numpy as np
tech=(
      {
      'Courses':['python','java','spark',np.nan,'cpp','hello','dotnet'],
      'Fee':[12.00,34.00,42.00,78.00,None,8.88,9.0],
      'Duration':["35_Days","45_Days",'55_Days','66_Days','77_Days','44_Days','33_Days'],
      'Discount':[10,20,30,40,50,60,70]
      }
      )
row_lables=['R0','R1','R2','R3','R4','R5','R6']
DD=pd.DataFrame(tech)
print(DD)

#Adding column in pandas dataframe
