# -*- coding: utf-8 -*-
"""
Created on Thu May 25 08:19:43 2023

@author: Nishant
"""

#normalizing unicode text to standard represenation
#you are working with unicode string but need to make sure
#that all of the string have
#the same underlying representation
s1= 'Spicy Jalape\u00f1o'
s2= 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
s1==s2
#output: False

# NFC: Nomalsation form canonical composition
# NFD: 
    
import unicodedata
t1 = unicodedata.normailze('NFC',s1)
t2 = unicodedata.normalize('NFC',s2)
t1 == t2
print(ascii(t1))
#output: 'Spicy Jalape\xf1o'
t3 = unicodedata.normailze('NFD',s1)
t4 = unicodedata.normalize('NFD',s2)
t3 == t4
#output:True
print(ascii(t3))
#output: 'Spicy Jalape\u030o'

######################################################
#normalization is an imporatnt part of any code that needs to ensure
#unicode text is a same and consistent way.this is especially true
#received as part of user input where you have little control of 
#normalization can also be an imporatant part of sanitizing anf fil

t1=unicodedata.normalize('NFD',s1)
''.join(c for c in t1 if not unicodedata.combining(c))
#Out: 'Spicy Jalapeno'
###################################################
#working with unicode character in regular expression
#you are using regular expression to process text

import re
num=re.complie('\d+')
#ASCII digits
num.match('123')
#<re.match object;span=(0, 3),match='123'>
#it's also important to be aware of special cases.for example,
#matching combined with case folding:
pat=re.compile('stra\u00dfe',re.IGNORECASE)
s = 'strße'
pat.match(s)


#stripping unwanted characters from string
'''
you want to strip unwanted character from  the beginning of the strin.
istrip() and rstrip() perform stripping from the left or right.
by defualt, thses methods strip whitespace 
# whitespace stripping
'''
s = '    hello world   \n'
s.strip()
#output: 'hello world'


#character stripping
t = '------hello====='
t.lstrip('-')
#output: 'hello====='

t = '------hello====='
t.strip('-=')
#output: 'hello'