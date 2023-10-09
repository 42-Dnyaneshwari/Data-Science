#set comprehesion
lst={x
     for x in range(3)
     }
print(type(lst))   #set
print(lst)

###############################
dic={x:x*x
     for x in range(3)
     }
print(type(dic))   #dictionary
print(dic)

################################
#*************GENERATOR****************
#it uses a object to access items and it use keyword yield
GEN=(x
     for x in range(3)
     )
print(type(GEN))   
print(GEN)
for i in GEN:
    print(i)
    
##################
#next method 
GEN=(x
     for x in range(3)
     )
print(GEN)
next(GEN)
##############
GEN=(x for x in range(3))
next(GEN)
next(GEN)
next(GEN)

#function which returns multiple values
def even(end):
    for i in range(0,end,2):
        yield i
for i in  even(6):
    print(i)
    
##################################
#instead of writing loop we use next method
gen=even(6)
next(gen) #0
next(gen) #2
next(gen) #4
next(gen) #StopIteration

#####################################
#chaining generaters
def lenght(itr):
    for ele in (itr):
        yield len(ele)
        
def hide(itr):
    for ele in itr:
        yield ele *'*'
passwd=['not-good',"give 'm-pass","00100=100"]
for passwd in hide(lenght(passwd)):
    print(passwd)

########################################
#print list with index
lst=['Hii','hello','how','are','you']
for i in range(len(lst)):
    print(i+1 ,lst[i])
    
#######################################
import string
#pick the adjectives
adjectives=['sleepy','slow','smelly','wet','fat','red','green','yello']
#pic the noun
nouns=['apple','dinosur','ball','goat','dragon','panda','duck']
#pick the words
import random
adjective=random.choice(adjectives)
noun=random.choice(nouns)
#select a number
number=random.randrange(0,100)
#select a special character
sep=random.choice(string.punctuation)
#create a new secure password
password=adjective + noun + str(number) + sep
print("password is:%s" % password)
#############################################3
#another one
#you  can use a while loop


##########################
import random
import string
adjectives=['sleepy','slow','smelly','wet','fat','red','green','yello']
#pic the noun
nouns=['apple','dinosur','ball','goat','dragon','panda','duck']
#pick the words
adjective=random.choice(adjectives)
noun=random.choice(nouns)
#select a number
number=random.randrange(0,100)
#select a special character
sep=random.choice(string.punctuation)
#create a new secure password
password=adjective + noun + str(number) + sep
print("password is:",password)

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
a=password         
if checkpass(a):
    print("STRONG")
else:
    print("WEAK") 