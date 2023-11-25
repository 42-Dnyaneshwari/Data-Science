# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:36:25 2023

@author: Nishant
"""
#importing the module psycopg2:pip install psycopg2
import psycopg2 as pg2

# creating the connection between python and PostgeySQL.
conn=pg2.connect(database='dvdrental', user='postgres' ,
                 host='localhost', password='root',
                 port=5432)

#Establising and starting the connection
cur=conn.cursor()

#Passing a sql query to cursor.
cur.execute('select *from payment')

#Only one record we will get.
cur.fetchone()

#Passing the no og recodes we want to get.
cur.fetchmany(10)

#Getting all the records present in payment tabale.
cur.fetchall()  

#after executing this only we can see table in pgadmin.
cur.commit()
#closing the cursor
cur.close()
############################################################


