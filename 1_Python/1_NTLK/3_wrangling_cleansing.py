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
Banner("Wrangling and cleansing")
# ===============================================================

import csv
with open('./output/word_frequency.txt', 'r') as f:
        reader = csv.reader(f,delimiter=',',quotechar='"')
        for line in reader:
            print('{}'.format(line[1])) #print second field

# ===============================================================
title("Parsing json")
jsonfile = open("./output/example.json", "r")
data = json.load(jsonfile)
print("Name is : {} {}".format(data["firstName"],data["lastName"]))
print("The address is : {}".format(data["address"]))

# ===============================================================
title("Text splitting")
inputstring="Although Douglas Crockford originally asserted that JSON is a strict subset of " \
            "JavaScript, his specification actually allows valid JSON documents that are invalid " \
            "JavaScript. Specifically, JSON allows the Unicode line terminators U+2028 LINE SEPARATOR " \
            "and U+2029 PARAGRAPH SEPARATOR to appear unescaped in quoted strings, while ECMAScript 2018 " \
            "and older does not. This is a consequence of JSON disallowing only control characters."
from nltk.tokenize import sent_tokenize
all_sent = sent_tokenize(inputstring)
print("Nltk senterce splitter algorithm: ")
print(all_sent)
# ===============================================================
title("Custom splitter")
import nltk.tokenize.punkt
tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()

# ===============================================================
title("Tokenization")
s = "Hi everyone !      hola gr8"
print(s.split())
from nltk.tokenize import word_tokenize
print("Nltk word_tokenize: {}".format(word_tokenize(s)))
from nltk.tokenize import regexp_tokenize, wordpunct_tokenize, blankline_tokenize
print("Regex tokenizer : {}".format(regexp_tokenize(s, pattern='\w+')))
print("Regex tokenizer : {}".format(regexp_tokenize(s, pattern='\d+')))
print("Wordpunkt tokenizer: {}".format(wordpunct_tokenize(s)))
print("Blank line tokenizer: {}".format(blankline_tokenize(s)))
# ===============================================================
title("Title stemming")
from nltk.stem import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer
pst = PorterStemmer()
lst = LancasterStemmer()
stm = SnowballStemmer(language="french")
print("Lancaster Stemmer on 'browing': {}".format(lst.stem("browning")))
print("Porter stemmer on 'eanting': {}".format(pst.stem("eating")))
print("Snowball stemmer on 'mangeais': {}".format(stm.stem("mangeais")))
# ===============================================================
title("Lemmatizer")
from nltk.stem import WordNetLemmatizer
wlem = WordNetLemmatizer()
print("Wordnet Lematizer: {}".format(wlem.lemmatize("eaten")))
print("Wordnet Lematizer: {}".format(wlem.lemmatize("colored")))
print("Wordnet Lematizer: {}".format(wlem.lemmatize("blushes")))
# ===============================================================
title("Stop-words removal")
from nltk.corpus import stopwords
stoplist = stopwords.words('english') #configure the language for stop words (22 languages supported)
text = "The city's landmarks include the Château Frontenac hotel that dominates the skyline, and the Citadelle of Quebec, an intact fortress that forms the centrepiece of the ramparts surrounding the old city and includes a secondary royal residence. The National Assembly of Quebec (provincial legislature), the Musée national des beaux-arts du Québec (National Museum of Fine Arts of Quebec), and the Musée de la civilisation (Museum of Civilization) are found within or near Vieux-Québec."
cleanwordlist = [word for word in text.split() if word not in stoplist] #that's a list
print("Wow! Very cool! {} words removed".format((len([x for x in text.split()]) - len([y for y in cleanwordlist]))))    #prints number of wrods removed
print(cleanwordlist)
# ===============================================================
title("Rare words removal")
# tokens in list of all tokens in corpus
token = cleanwordlist
freq_dist = nltk.FreqDist(token)
rarewords= list(freq_dist.keys())[-50:]
#after_rare_words = [word for word in token not in rarewords]
#not working somewhow
# ===============================================================
title("Spell correction")
from nltk.metrics import edit_distance
string1 = "rain"
string2 = "shine"
print("Edit distance between edit_distance '{}' and '{}' is {}".format(string1, string2, edit_distance(string1, string2)))
# ===============================================================


# ===============================================================


# ===============================================================


# ===============================================================


# ===============================================================


# ===============================================================


# ===============================================================


# ===============================================================


# ===============================================================


# ===============================================================

# ===============================================================


# ===============================================================


# ===============================================================


# ===============================================================


# ===============================================================


# ===============================================================

Banner("Good bye")