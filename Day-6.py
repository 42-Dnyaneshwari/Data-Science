print("Hello, Dnyaneshwari \n Good Morning")
#scope of variable
x=x+1
x=9
#file handling
f1=open("p.txt",'r')
print(f1.read())

#using relative path
with open("p.txt") as obj:
    c=obj.read()
print(c)

#to reduce gap of output screen
with open("p.txt") as obj:
    c=obj.read()
print(c.rstrip())

#using absolute path
f1='C:/1-Python/p.txt'
with open(f1) as obj:
    c=obj.read()
print(c.rstrip())

#read line by line
f1='p.txt'
with open(f1) as obj:
    for line in obj:
        print(line)

#using rstrip
f1='p.txt'
with open(f1) as obj:
    for line in obj:
        print(line.rstrip())
        
#list of lines
f1='p.txt'
with open(f1) as obj:
        lines=obj.readlines()
for line in lines:   
        print(line.rstrip())

#to genrate random lotery no
from random import randrange
mn=1
mx=49
num_nums=6
tn=[]
for i in range(num_nums):
    #gnrate list that is not present
    rand=randrange(mn,mx+1)
    while rand in tn:
        rand=randrange(mn,mx+1)
    tn.append(rand)
tn.sort()
for n in tn:
    print(n,end=" ")    
    print()    
    
#outliers are the extrem values
v=[89,105,7,4,12,33]
r=sorted(v)
def rem_out(data,num_out):
    r=sorted(data)
    for i in range(num_out):
        r.pop(-1)
    return r
rem_out(v,2)
       
#assignment6 pass is good or not :(
def checkpass(password):
    hu=False
    hl=False
    hn=False
    for ch in password:
        if ch>='A' and ch<='Z':
            hu=True
        elif ch>='a' and ch<='z':
            hl=True
        elif ch>='0' and ch<='9':
            hn=True
    if len(password)>=8 or hu==True or hl==True or hn==True:
        return True
    else:
        return False
a=input("enter the password:")         
if checkpass(a):
    print("Strong")
else:
    print("Weak")