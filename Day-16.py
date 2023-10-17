# -*- coding: utf-8 -*-
"""
Created on Fri May  5 08:15:53 2023

@author: Dnyaneshwari...
"""
###########################################
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
df=pd.DataFrame(tech)
print(df)
#######################################################33

#Adding column to pandas dataframe

tutors=['ram','sham','megha','ravi','hell','pani','tani']
df2=df.assign(TutorsAssigned=tutors)
print(df2)
##############################################

#adding multiple columns to pandas DataFrame
MNCCompanies=['Tata','Bata','HCL','TCS','Heaven','Google','HELLO']
df2=df.assign(MNCComp=MNCCompanies,TutorsAssigned=tutors)
df2
#####################################################

#derive column from existing column
df=pd.DataFrame(tech)
df2=df.assign(Dis_per=lambda x : x.Fee * x.Discount / 100)
print(df2)
######################################

#append column to an existing dataframe
df2['MNCC']=MNCCompanies
df2
#########################################################

#add column add specific position
df=pd.DataFrame(tech)
df.insert(0,'Tutors',tutors)
print(df)
###################################################

#pandas rename columns with example
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
df=pd.DataFrame(tech)
print(df)
###################################################
print(df.columns)
df.dtypes
df2=df.rename(columns={'Courses':'Courses_List'})
print(df2.columns)
##################################################

#u can also rename() using axis=1 or axis='columns
df2=df.rename({'Courses':'Courses_List'},axis=1)

df2=df.rename({'Courses':'Courses_List'},axis='columns')

print(df2)

#replace existing datafram with inplace=True which returns None
df2=df.rename({'Courses':'Courses_List'},axis=1,inplace=True)
df.columns