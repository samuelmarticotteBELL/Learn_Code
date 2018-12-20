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
Banner("Building NLP apps")
# ===============================================================
title("Summarizin a news article")

import sys
f=open('input/news_article.txt','r')
news_content=f.read()
import nltk


results = []
for sent_no,sentence in enumerate(nltk.sent_tokenize(news_content)):            #for all sentences
    no_of_tokens = len(nltk.word_tokenize(sentence))
    print("Sentence #{}: {}".format(sent_no,sentence))#tokenize sentence
    print("Tokens: {}".format(no_of_tokens))
    tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    no_of_nouns = len([word for word,pos in tagged if pos in ["NN","NNP"]])     #count # of nouns in sentences
    print("Nouns: {}".format(no_of_nouns))
    ners=nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence)),binary=False) #NEF to tag named entities
    no_of_ners = len([chunk for chunk in ners if hasattr(chunk, 'label')])
    print("Named entities: {}".format(no_of_ners))
    score =(no_of_ners+no_of_nouns)/float(no_of_tokens)
    print("Score: {}".format(score))
    results.append((sent_no, no_of_tokens, no_of_nouns, no_of_nouns, score, sentence))
    print("=============================================")

title("Results of sentence ranking")
for sent in sorted(results,key=lambda x: x[4],reverse=True):
    print(sent[5])

title("Improving with scikit")

import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
results2 = []

sentences = nltk.sent_tokenize((news_content))

vectorizer = TfidfVectorizer(norm='l2',min_df=0, use_idf=True, smooth_idf=False, sublinear_tf=True)

sklearn_binary = vectorizer.fit_transform(sentences)

print(vectorizer.get_feature_names())

print(sklearn_binary.toarray())
for i in sklearn_binary.toarray():
    results2.append(i.sum()/float(len(i.nonzero()[0])))


print(results2)
# ===============================================================

Banner("Good bye")