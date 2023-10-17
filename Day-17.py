# -*- coding: utf-8 -*-
"""
i
@author: Dnyaneshwari...
"""
import pandas as pd
import numpy as np
data={
      "A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
      }
df=pd.DataFrame(data)
print(df)
#####################################################

#quick way to get no of row count
row_count=len(df.index) #7
row_count=len(df.axes[0]) #7

#to return no of rows
row_count=df.shape[0] #7
#to return no of columns
col_count=df.shape[1] #4
print("column count is:",col_count)
print("rows count is:",row_count)
#######################################################

#pandas apply() function to columns

import pandas as pd
import numpy as np
data={
      'A':[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
      }
df=pd.DataFrame(data)
print(data)

#adding 3 in all the columns
def add_3(x):
    return x+3
df2=df.apply(add_3)
print(df2)

#multipy by 3 to columnn B
def mul_3(x):
    return x*3
df2["B"]=df["B"].apply(mul_3)
print(df2['B'])

#apply() on multiple columns i.e. 
#adding 4 into column A,B.
def add_4(x):
    return x+4
df2[["A","B"]]=df[["A","B"]].apply(add_4)
print(df2[["A","B"]])

# apply() lamda funtion to each column on pandas dataframe
df2=df.apply(lambda x : x +10)
print(df2)

#lambda funtion single column
df2["C"]=df["C"].apply(lambda x : 10 - x)
print(df2["C"])

#transfrom() ,sum()
#same as apply()
def mul_3(x):
    return x*3
df2=df.transform(mul_3)
print(df2)
################################
df2["A"]=df["A"].map(lambda x : x +10)
print(df2["A"])

#using numpy funtion on single column 
#using dataframe.apply() and [] operator
import numpy as np
df2['A']=df['A'].apply(np.square)
print(df2)
########################################################

#USING NUMPY.SQUARE FUNTION
df['A']=np.square(df['A'])
print(df['A'])
##################################

#using pandas groupby() 
import pandas as pd
import numpy as np
tech=(
      {
      'Courses':['python','python','spark',None,'cpp','hello','dotnet'],
      'Fee':[12.00,78.00,78.00,78.00,None,8.88,9.0],
      'Duration':["35_Days","35_Days",'35_Days','66_Days','77_Days','44_Days','33_Days'],
      'Discount':[10,10,10,40,50,60,70]
      }
      )
row_lables=['R0','R1','R2','R3','R4','R5','R6']
df=pd.DataFrame(tech)
print(df)

#groupby()
#single funtion
df2=df.groupby(['Fee']).sum()
print(df2)
######################################################
#for multiple columns
df2=df.groupby(['Courses','Fee']).sum()
print(df2)
##############################################

#add an index to dataframe
#reset_index()
#group bu single columns
df2=df.groupby(['Courses','Fee']).sum().reset_index()
print(df2)
#####################################################

#group by multiple cilumns
df2=df.groupby(['Courses','Fee']).sum()
print(df2)
#######################################]

#pandas dataframe to get columns name
import pandas as pd
import numpy as np
tech=(
      {
      'Courses':['python','python','spark',None,'cpp','hello','dotnet'],
      'Fee':[12.00,78.00,78.00,78.00,None,8.88,9.0],
      'Duration':["35_Days","35_Days",'35_Days','66_Days','77_Days','44_Days','33_Days'],
      'Discount':[10,10,10,40,50,60,70]
      }
      )
row_lables=['R0','R1','R2','R3','R4','R5','R6']
df=pd.DataFrame(tech)
print(df)
df.columns
#get the name of column from headers
column_headers=list(df.columns.values)
print("the column header is:",column_headers)
#using list(df.columns)
column_headers=list(df.columns)
print("the column header is:",column_headers)
#using list(df)
column_headers=list(df)
print("the column header is:",column_headers)
#####################################################

#wenever there are less accuracy we go for shuffling 
#because after that we will get accurate answer
#shuffling of rows in pandas DataFrame
#SHUFFLE ALL ROWS AND RETURN ALL ROWS
df1=df.sample( frac=1)
print(df1)
###################################################### 

#create a new index starting from zero
df1=df.sample( frac=1).reset_index()
print(df1)
###################################################

#drop shuffle index
df1=df.sample(frac=1).reset_index(drop=True)
print(df1)
####################################################

#
