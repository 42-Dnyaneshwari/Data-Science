# -- coding: utf-8 --
"""
Created on Mon Jan 29 14:40:57 2024

@author: Dnyaneshwari
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
email_data=pd.read_csv("C:/3-Naive Bayes/sms_row.csv",encoding="ISO-8859-1")

import re
def cleaning_text(i):
    w=[]
    i=re.sub("{^A-Za-z""}+"," ",i).lower()
    for word in i.split(" "):
        if len(word)>3:
            w.append(word)
    return (" ".join(w))

cleaning_text("Hope you are having a good week. Just checking in")

email_data.text=email_data.text.apply(cleaning_text)
email_data=email_data.loc[email_data.text!="",:]

from sklearn.model_selection import train_test_split
email_train,email_test=train_test_split(email_data,test_size=0.2)

def split_into_words(i):
    return [word for word in i.split(" ")]


emails_bow=CountVectorizer(analyzer=split_into_words).fit(email_data.text)
all_emails_matrix=emails_bow.transform(email_data.text)

train_emails_matrix=emails_bow.transform(email_train.text)
test_emails_matrix=emails_bow.transform(email_test.text)

tfidf_Transformer=TfidfTransformer().fit(all_emails_matrix)
train_tfidf=tfidf_Transformer.transform(train_emails_matrix)
test_tfidf=tfidf_Transformer.transform(test_emails_matrix)

test_tfidf.shape


from sklearn.naive_bayes import MultinomialNB as MB
classifer_mb=MB()
classifer_mb.fit(train_tfidf,email_train.type)

test_pred_m=classifer_mb.predict(test_tfidf)
accuracy_test_m=np.mean(test_pred_m==email_test.native)
accuracy_test_m
###############################################################



