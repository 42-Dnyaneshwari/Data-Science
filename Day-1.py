
print("hello everyone")

#type casting
x = 1
print(x)
print(type(x))
age=int(input("enter a:"))
print(type(age))
print(age)

#complex values
c1=1
c2=2j
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

#boolean values
all_ok=True
print(all_ok)
all_ok=False
print(all_ok)
print(type(all_ok))

#converting bool to string
status=bool(input("enter anything:"))
print(status)
print(type(status))

#arithmatic operator
home=100
away=13
print(home + away)
print(type(home + away))
print(home / away)
print(type(home / away))
print(home % away)
print(type(home % away))

#power 
a=5
b=3
print(a**b)

#assignment operator
x=0
x+=1

#None values
winner=None
print(type(winner))
print((winner is None))
print((winner is not None))

#flow control statements
#comparision operator
num=int(input("enter num:"))
if num>0:
    print(num) 
#if else statement
num=int(input("enter num:"))
if num<0:
    print(num,"is negative") 
else:
    print(num,"is positive")
#if elif else
saving=float(input("enter your savings:"))
if saving==0:
    print("sorry you are not having savings")
elif saving<500:
    print("well done")
elif saving<1000:
    print("thats a tidy sum")
elif saving<10000:
    print("very good :)")
else:
    print("thank you for saving money")
    
#while loop
count=1
print("starting")
while (count<10):
    print(count)
    count+=1
#for loop
for i in range(0,11):
    print(i)
print("done")
#break 
num=int(input("enter num:"))
for i in range(0,16):
    if i==num:
        break
    print(i)
print("done")

#anonymous loop variable
for _ in range(0,10):
    print("$",end="")
    print()
    
#Assignment 1
#1)
ht=float(input("enter height:"))
wt=float(input("enter weight:"))
BMI=round((wt/(ht*ht)),2)
if BMI<18.5:
    print("you are under weight",BMI)
elif BMI>18.5:
    print("you are normal weight",BMI)
elif BMI>25 and BMI<30:
    print("you are over weight",BMI)
elif BMI>30 and BMI<35:
    print("you are obese weight",BMI)
elif BMI>35:
    print("you are clinically obese",BMI)
else:
    print("thank you :)")

#2)
ht=int(input("enter height:"))
if ht>=120:
    print("you are allow to sit in the roller coster")
    age=int(input("enter age:"))
    bill=0
    if age<12:
        print("childs ticket is 5$")
        bill=5
    elif age>12 and age<18:
        print("childs ticket is 7$")
        bill=7
    elif age>18 and age<45:
        print("students ticket is 12$")
        bill=12
    elif age>45 and age<55:
        print("your ticket is 15$")
        bill=15
    w=input("want pic:")
if w=='Y':
    bill=bill+3
    print("so now your totakl pic:",bill)
else:
    print("your bill is without pic:",bill)
    exit

        
