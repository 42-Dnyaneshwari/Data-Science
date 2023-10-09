
# WORKING WITH THE JSON 
##################
#Soring Data
import json
num=[1,2,3,4,5]
fn="num.json"
with open(fn,'w') as f:
    json.dump(num,f)
################################

#SAVING DATA WITH JSON 
#WHEN YOU ARE WORKING WITH THE USER GENRATED DATA
import json
username=input("enter name:")
fn="user.json"
with open(fn,'w') as f:
    json.dump(username,f)
print("we will remember you :)")  
######################################

#A PROGRAM WHO'S ANME IS ALREADY STORED IN THE JSON FILE
import json
username=input("enter name:")
fn="user.json"
with open(fn) as f:
    username=json.load(f)
print("we will remember you :)",username)  
#########################################

#COMBINE BOTH 
import json
fn='user.json'
try:
    with open(fn) as f:
        username=json.load(f)
except FileNotFoundError:
    username=input("enter name:")
    with open(fn,'w') as f:
        json.dump(username,f)
        print("we will remember you :)",username)
else:
    print("welcome back....",username)
 
#****************LIST COMPRESSION*****************
#CODE OPTIMIZATION
#1
lst=[]
for i in range(0,20):
    lst.append(i)
print(lst)
#2
lst=[i for i in range(0,20)]
print(lst)

#using list comprehesion  
# to captilize the intitial of words
names=['dada','kaka','mama','baba']
lst={i.capitalize() for i in names}
print(lst)

#list comprehesion using if amd else
def even(num):
    return num%2==0
lst=[
     num
     for num in range(10)
     if even(num)
     ]
print(lst)
##########
lst=[f"{x}{y}"
     for x in range(3)
     for y in range(3)
     ]
print(lst)

###########
lst=[f"{x}{y}{z}"
     for x in range(3)
     for y in range(3)
     for z in range(3)
     ]
print(lst)

#############
