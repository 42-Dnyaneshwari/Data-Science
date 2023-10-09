#working with a file'contents
#after you have read a file into memory you can do whatever you want with that data
filename = 'sample.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()
        print(pi_string)
        print(len(pi_string)) 

#Writing to a file
#one of the simplex way to store the data is to write it to a file. 
#when you write text to a file, the output will still be available after you close the terminal containing your programs output.
filename = 'programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I LOVE SHIVJANMABHOOMI")
    
#writing multiple
#The write() function doesn't add any newlines to the text you write. 
    
filename = 'programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I LOVE SHIVJANMABHOOMI \n")
    file_object.write("I LOVE MY JUNNAR")
#appending the contet of file
f1='p.txt'
with open(f1,'a') as obj:
    obj.write("\nHey,its DD")

##############################################    
#Exception Handling
print(5/0) #ZeroDivisionError

#using try and except block
try:
    print(4/0)
except ZeroDivisionError:
    print("can not divide by zero!")

#using exception to prevent crashes
print("enter two no for division")
print("enter 'q' tp quit")
while True:
    f=input("enter 1st no:")
    if f=='q':
        break
    s=input("enter 2nd no:")
    if s=='q':
        break
    ans=int(f)/int(s)
    print(ans)
    
#FileNotFound 

f1='alice.txt'
with open(f1,encoding='utf-8') as f:
    c=f1.read()
########################################
f1='alice.txt'
try:
    with open(f1,encoding='utf-8')as f:
        c=f1.read()
except FileNotFoundError:
    print("sorry can not open a file")     


