
#location of print is change
num=int(input("enter num:"))
for i in range(0,6):
    if i==num:
        break
    print(i,'',end="")
print("done")

#############################
num=int(input("enter num:"))
for i in range(0,6):
    if i==num:
        break
    print(i,' ',end="")
    print("done")
   
#Tuple
tup=(1,2,3,4,5)
print("ele 1:",tup[0])
print("ele 2:",tup[1])
print("ele 3:",tup[2])
print("ele 4:",tup[3])
print("ele 5:",tup[4])

#tuple can hold diff datatype
tup=('hello',123,'this is',56.7)
print(tup)

#iterating a tuple over a for loop
tup=('hello',123,'this is','python')
for i in tup:
    print(i)
    
#tuple related fuction
tup=('hello',123,'this is','python')
print("lenght:",len(tup))
print("count of 1 is:",tup.count('hello'))
print("index of ele 1 is:",tup.index(123))
if 123 in tup:
    print("123 is present")
else:
       print("123 is not present") 
#nested tuple
tup1=('hello',23,23.4)
tup2=("hey",56,-42)
tup3=(1,"oyee",tup1,tup2,'hoyee')
print(tup3)

#list.....
lst2=[1,'happy',-3,4.5,True]
lst1=['lisa',13,'suga',False]
lst=['start',lst2,lst1,'end']
print(lst)

#extend
print("after extend list is:")
lst.extend("school")
print(lst)

#append
print("after append list is:")
lst.append('Blackpink')
print(lst)

#insert
print("after insert at index 2 list is:")
lst.insert(2,'starting_na...')
print(lst)

#traverse the list
print("element of location -1 is:",lst[-1])
print("element of location -0 is:",lst[0])

#concatenation
lst=lst1+lst2
print(lst)

#change element
lst=[1,2,3,4,5,6,7,8,9]
for i in range(-3,-1):
    print(lst)
    
###program for duplicate element 
lst=[1,2,3,4,5,5,6,7,8,9]
def is_duplicate(lst):
    for i in range(len(lst)-1):
        if(lst[i]==lst[i+1]):
            return True
    return False
print(is_duplicate(lst))

#mario pyramid
for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()
    
for i in range(4):
    for j in range(4-i):
        print("*",end=" ")
    print()
    
#Assighnment 2
#1) pelimdrom  
def peli(x):
    return x==x[::-1]
x=input("enter string:")
ans=peli(x)
if ans:
    print("Yes...")
else:
    print("Noo...")
    
#2)min and maX value of a list
lst=[]
for i in range(0,9):
    lst.append(i)
print(lst)
max=0
for j in lst:
    if j>max:
        max=j
print("max",max)

min=0
for j in lst:
    if j<min:
        min=j
print("min",min)

