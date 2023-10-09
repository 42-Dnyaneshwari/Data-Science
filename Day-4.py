
#function to get all values , keys, items
dic={'Student':'Dnyaneshwari','Rno':'42','Div':'A'}
print(dic.values()) 
print(dic.keys())
print(dic.items())

#membership operator
dic={'Student':'Dnyaneshwari','Rno':'42','Div':'A'}
print('Div'in dic)
print('Rno' not in dic)

#dictionary  can have values as tuple 
s={'day':('mon','tues','wed'),'date':(11,12,13),'year':('2022','2023','2024')}
print(s['day'])
print(s['day'][1])

#dictionary can have values as list
s={'day':['mon','tues','wed'],'date':[11,12,13],'year':['2022','2023','2024']}
print(s['date'])

#get() vakues using method
print(dic.get('42'))

#DICTIONARY CAN NOT HAVE DUPLICATE VALUES
dic={'brand':'BMW','model':'breezaa','year':'2023','year':'2022'}
print(dic)

#loop throught dict
for x in dic:
    print(x)          #for keys
    print(dic[x])      #for values
#for values to access   
for x in dic.values():
    print(x)
#for keys to access
for x in dic.keys():
    print(x)

#copy of dictionary     
for x,y in dic.items():
    print(x,y)
mydict=dic.copy()
print(mydict)

#functions

#1.prime number
def pri(num):
    for i in range(2,num):
        if (num%i==0):
            return 'NOT PRIME'
    return 'PRIME'
print(pri(13))
#2.hello
def hell():
    print('hello guys....')
hell()
#3.pet
def pet(d,m):
    print('I hvae a',d)
    print("His name is",m)
pet('dog','lucky')
#default values
def pet(d='Dog',m):
    print('I hvae a',d)
    print("His name is",m)
pet(m='lucky')

#assignmnet3
#anagram program 
def ana(s1,s2):
    
    a=list(s1.replace("","").lower())
    b=list(s2.replace("","").lower())
    if(len(a)!=len(b)):
        return False
    else:
        return (sorted(a)==sorted(b))
ana('bad','dad')

#sum of num divisible by 5,7
#using ir
l=[1,22,35,48,50,8,9] 
def sum(l):
    s=0
    for i in range(len(l)):
        if(l[i]%5==0 or l[i]%7==0):
            s=s+l[i]
    return s
print(sum(l))
#using and
l=[1,22,35,48,50,8,9] 
def sum(l):
    s=0
    for i in range(len(l)):
        if(l[i]%5==0 and l[i]%7==0):
            s=s+l[i]
    return s
print(sum(l))

#assignment 4
def reverse_words(input):
    if input=="":
        return 'wrong input'
    else:
        words=input.split()
        reverse_sentence="".join(reversed(words))
    return reverse_words
print(reverse_words("this is india"))


    