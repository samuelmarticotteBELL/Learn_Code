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
Banner("Parsing text structure")
# ===============================================================
title("Toy context free grammar")
from nltk import CFG
toy_grammar = nltk.CFG.fromstring(
"""
    S -> NP VP                  
    VP -> V NP
    V -> "eats" | "drinks" 
    N -> Det N                  
    Det -> "a" | "an" | "the" 
    N -> "president" | "Obama" | "apple" | "coke" 
""")
toy_grammar.productions()
# ===============================================================
title("Regex Parser")
import nltk
from nltk.chunk.regexp import *
chunk_rules=ChunkRule("<.*>+", "chunk everything")
reg_parser = RegexpParser('''
    NP : {<DT>? <JJ>* <NN>*}
    P : {<IN>}
    V: {<V.*>}
    PP:{<P> <PP>}
    VP:{<V> <NP|PP>*}
''')
test_sent = "Mr Obama played a big role in the Health insurance bill"
test_sent_pos=nltk.pos_tag(nltk.word_tokenize(test_sent))
parsed_out=reg_parser.parse(test_sent_pos)
print(parsed_out)
# ===============================================================


# ===============================================================


# ===============================================================


# ===============================================================


# ===============================================================

Banner("Good bye")