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
Banner("Welcome to nltk")

# ===============================================================

title("Basic string commands")
lst=[1,2,3,4]
print(str(lst))
print('First element: ' + str(+lst[0]))
print('First three elements: ' + str(lst[0:3]))
print('Last three elements: ' + str(lst[1:4]))
title("Help commands : dir() and help()")
print("Functions that can apply to type list: \n" + str(dir(str)))
#===============================================================
title("Split and strip")
mystring = "Monty Python! And the holy grail! \n"
print("Split: " + str(mystring.split()))
print("Strip: " + str(mystring.strip()))
print("Print string in upper case: " + str(mystring.upper()))
print("Replace ! with nothing: " + str(mystring.replace('!', '''''')))
#===============================================================
title("Regular expressions")
if re.search('Python', mystring):
    print("We found Python in the string: " + mystring)
else:
    print("We did not found 'Python'")
print('Find all patterns of ! in string: ' + str(re.findall('!', mystring)))
#===============================================================
title('Writing a function')


def wordfreq (mystring):
    '''
    Function to generate the frequency distribution of the given text
    '''
    print(mystring)
    word_freq={}
    for token in mystring.split():
        if token in word_freq:
            word_freq[token]+=1
        else:
            word_freq[token]=1
    print(word_freq)


str = "This is my first python program"
wordfreq(str)


# ===============================================================
Banner("Good bye")