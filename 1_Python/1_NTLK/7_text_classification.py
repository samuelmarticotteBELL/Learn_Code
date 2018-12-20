#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# To compile: python ./name.py
# For libraries: pipenv install <package>
# pip install pyfiglet / conda install -c conda-forge pyfiglet
import sys, os
from pyfiglet import Figlet  # banners
import re  # regulare expressions
import urllib3
import requests
import nltk
from nltk.corpus import stopwords

set(stopwords.words('english'))
from bs4 import BeautifulSoup
import string
from wordcloud import WordCloud
import csv
import json


#####------------------------------------------------(Constants)
# arguments=
# name=
# path=
# version=1.0

def Banner(text):
    banner = Figlet(font='slant')
    print(banner.renderText(text))


def welcome():
    Banner('Program')
    print('Usage: program [option]')


def goodbye():
    Banner('GoodBye')
    exit()


def title(title):
    print('\033[1;33m---------------%s---------------\033[1;m\n' % title)


#### Main menu----------------------------------------(Main Menu)
Banner("Text Classification")
# ===============================================================
title("Let's clean the text")

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import csv

#Preprocessing function

def preprocessing(text):
    #print("Preprocessing: {}".format(text))

    # tokenize into words
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]

    # remove stopwords
    stop = stopwords.words('english')
    tokens = [token for token in tokens if token not in stop]

    # remove words less than three letters
    tokens = [word for word in tokens if len(word) >= 3]

    # lower capitalization
    tokens = [word.lower() for word in tokens]

    # lemmatize
    lmtzr = WordNetLemmatizer()
    tokens = [lmtzr.lemmatize(word) for word in tokens]
    preprocessed_text=' '.join(tokens)

    return preprocessed_text


#Cleaning the spam collection

i = 0
with open('input/sms.csv', encoding='utf-8') as sms:
    sms_data = []
    sms_labels = []
    csv_reader = csv.reader(sms, delimiter=';')
    for line in csv_reader:
        #print(line[1])
        # adding the sms_id
        sms_labels.append(line[0])
        # adding the cleated text We are calling preprocessing method
        sms_data.append(preprocessing(line[1]))

    print("Sms_data: {}".format(sms_data))
    # ===============================================================
    title("Let's train with data")
    import sklearn
    import numpy as np

    trainset_size = int(round(len(sms_data) * 0.70))
    # i chose this threshold for 70:30 train and test split.
    print('The training set size for this classifier is ' + str(trainset_size) + '\n')
    x_train = np.array([''.join(el) for el in sms_data[0:trainset_size]])
    y_train = np.array([el for el in sms_labels[0:trainset_size]])
    x_test = np.array([''.join(el) for el in sms_data[trainset_size + 1:len(sms_data)]])
    y_test = np.array([el for el in sms_labels[trainset_size + 1:len(sms_labels)]])

    print("This is x_train:\n{}".format(x_train))
    print("This is y_train:\n{}".format(y_train))

    # ===============================================================
    title("Let's generate a term-document matrix")


    from sklearn.feature_extraction.text import CountVectorizer
    sms_exp=[]
    for line in sms_data:
            sms_exp.append(preprocessing(line))
    vectorizer = CountVectorizer(min_df=1)
    print("Sms exp:\n {}".format(sms_exp))
    X_exp = vectorizer.fit_transform(sms_exp)
    print("Feature names:")
    print("||".join(vectorizer.get_feature_names()))
    print(X_exp.toarray())
# ===============================================================


# ===============================================================


# ===============================================================


# ===============================================================


# ===============================================================


# ===============================================================



# ===============================================================
sms.close()
Banner("Good bye")