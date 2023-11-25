# -*- coding: utf-8 -*-
"""
Created on Fri May 26 08:19:59 2023

@author: Dnyaneshwari...
"""
#############################################
#sentence tokenization
import nltk
nltk.download('punkt')
sentence_data="The first sentence is about python.the second is about nltk"
nltk_tokens=nltk.sent_tokenize(sentence_data)
print(nltk_tokens)
#error
####################
#non english 
import nltk
german_tokenizer=nltk.data.load('tokenizers/punkt/german.pickle')
german_tokens=german_tokenizer.tokenize('Wie geht es Ihen? danke.')
print(german_tokenizer)
##########################################

#word tokenizer
import nltk
from nltk import word_tokenize
word_data='hello everyone what are you doing? I Hope you are fine!!!'
nltk_tokens=nltk.word_tokenize(word_data)
print(nltk_tokens)
######################################
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords.words('english')
from nltk.corpus import stopwords
en_stops=set(stopwords.words('english'))
all_words=['Threre','Is','a','tree','the','river']
for word in all_words:
    if word not in en_stops:
        print(word)
###################################################       
import nltk
nltk.download('omw-1.4') 
from nltk.corpus import wordnet
synonyms=[]
for syn in wordnet.synsets('soil'):
    for lm in syn.lemmas():
        synonyms.append(lm.name())
print(set(synonyms))
##################################################
import nltk
nltk.download('omw-1.4') 
from nltk.corpus import wordnet
antonyms=[]
for syn in wordnet.synsets('ahead'):
    for lm in syn.lemmas():
        antonyms.append(lm.antonyms()[0].name())
print(set(antonyms))
#####################################################