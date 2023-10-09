#return values
def get(fn,ln):
    full=f"{fn} {ln}"
    return full
m=get("sam","jam")
print(m)

#function can return a dictionary
def build_person(fn,ln):
    person={'f':fn,'last':ln}
    return person
m=build_person('Dnyaneshwari','Dolzake')
print(m)

#passing a list to a fuction
def user(names):
    for name in names:
        msg=f"hello,{name.title()}!"
        print(msg)
username=['sam','ram','jam']
user(username)

#passing a arbitary argument
def pizza(*topping):
    print(topping)
pizza("base")
pizza("corn","cheese","red chili")

#using loop
def pizza(*topping):
    for i in topping:
        print(i)
pizza("base")
pizza("corn","cheese","red chili")

#mixing position with arbitary 
#here size is a positional arg and topping is arbitary arg
def pizza(size,*topping):
    print("size for making pizza is:",size)
    for i in topping:
        print(i)
pizza(5,"base")
pizza(9,"corn","cheese","red chili")

#importing a module or function
#1
import pizza
pizza.make_pizza(3,'base')

#2
from pizza import make_pizza
make_pizza(4,"corn","cheese","red chili")

#3 :( ALIAS )
from pizza import make_pizza as mp
mp(4,"corn","cheese","red chili")

#4
import pizza as p
p.make_pizza(4,"corn","cheese","red chili")

#5
from pizza import *
make_pizza(4,"corn","cheese","red chili")


#leap year
def ly(y):
    if (y>0 and y%100==0 and y%400==0):
        print(y,"is a leap year")
    elif (y%4==0 and y%100!=0):
        print(y,"it is a leap year")
    else:
        print(y,"is not a leap year")
ly(2016)

#genrate and display password using ramdom
from random import randint
SHORTEST=7
LONGEST=10
MAX_ASCII=120
MIN_ASCII=33
def gen_pass():
    randomlenght=randint(SHORTEST,LONGEST)
    res=" "
    for i in range(randomlenght):
        randomchar=chr(randint(MIN_ASCII,MAX_ASCII))
        res=res+randomchar
    return res
print("your random password is:",gen_pass())
        
#Assignment 5
#sum of fibonnacci series
def fi(n):
    if n<0:
        print("incorrect input")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fi(n-1)+fi(n-2)
print(fi(9))