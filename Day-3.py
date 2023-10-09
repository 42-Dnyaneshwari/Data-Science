#list operations
#remove
lst=['oooo','ffff','gggg','tttt','rrrrr']
lst.remove('ffff')
print(lst)
#pop
lst.pop(0)
print(lst)

#set
#accessing elements of a set
bas={'what','the','hell','what'}
print(bas)
for i in bas:
    print(i)
#adding elements in set
b={'1','2','3','4','5'}
print(b)
#add
b.add('6')
print(b)
#update
b.update('7','8','9','0')
print(b)
#len
print(len(b))
#remove
b.remove('0')
print(b)
#discard
b.discard('1')
print(b)
#min and max
print(max(b))
print(min(b))

#set operation
s1={'hello','how','are','you'}
s2={'i','am','okay...'}
print('union:',s1|s2)
print("intersection:",s1&s2)
print("difference:",s1-s2)

#Dictionary....
dic={'Student':'Dnyaneshwari','Rno':'42','Div':'A'}
print(dic)
#accessing item using key
print('dic[Student=]',dic['Student'])
dic['Div']='B'
print(dic)
#deleting
del dic['Div']
dic.pop('Student')
print(dic)
print(len(dic))

#Accessing
dic={'Student':'Dnyaneshwari','Rno':'42','Div':'A'}
for i in dic:
    print(i,end=' , ') #only key is display
    print(dic[i]) #both key and value is display

