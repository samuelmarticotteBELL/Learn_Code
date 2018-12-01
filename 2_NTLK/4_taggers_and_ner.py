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
Banner("POS tagger and Named entity recognition")
text = "The city's landmarks include the Château Frontenac hotel that dominates the skyline, and the Citadelle of Quebec, an intact fortress that forms the centrepiece of the ramparts surrounding the old city and includes a secondary royal residence. The National Assembly of Quebec (provincial legislature), the Musée national des beaux-arts du Québec (National Museum of Fine Arts of Quebec), and the Musée de la civilisation (Museum of Civilization) are found within or near Vieux-Québec."
# ===============================================================
title("Part of speech tagging")
from nltk import word_tokenize
s = "I was watching TV"
#nltk.download('averaged_perceptron_tagger')
print("We will tokenize this phrase {}\n{}".format(s, nltk.pos_tag(word_tokenize(s))))
# ===============================================================
title("Look for all the nouns via POS")
tagged = nltk.pos_tag(word_tokenize(text))
allnoun = [word for word,pos in tagged if pos in ['NN', 'NNP']]
allverbs = [word for word,pos in tagged if pos in ['VB','VBG','VBD','VBN']]
print("These are all the nouns of {}".format(allnoun))
print("These are all the verbs of {}".format(allverbs))
# ===============================================================
title("Stanford tagger")
from nltk.tag.stanford import CoreNLPPOSTagger
core_nlp_tagger = CoreNLPPOSTagger()
tokens = nltk.word_tokenize(text)
#print("This is the core NLP tagger: {} ".format(core_nlp_tagger.tag(token)))
# ===============================================================
title("Building a custom POS tagger")
from nltk.corpus import brown
#nltk.download('brown')
tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
#Display most frequent part of speech in news corpus
print(sorted(nltk.FreqDist(tags).items(),reverse=True,key=lambda item: (item[1], item[0])))
# ===============================================================
title("Benchmarking a tagger")
brown_tagged_sents = brown.tagged_sents(categories='news')
default_tagger = nltk.DefaultTagger('NN')
#How to benchmark a tagger against the brown corpus for validation
print(default_tagger.evaluate(brown_tagged_sents))
# ===============================================================
title("N-Gram Parsers")
from nltk.tag import UnigramTagger
from nltk.tag import DefaultTagger
from nltk.tag import BigramTagger
from nltk.tag import TrigramTagger

#We divide the data into test and train data to evaluate our taggers
train_data = brown_tagged_sents[:int(len(brown_tagged_sents) * 0.9)]
test_data = brown_tagged_sents[int(len(brown_tagged_sents) * 0.9):]
unigram_tagger = UnigramTagger(train_data, backoff=default_tagger)
print(unigram_tagger.evaluate(test_data))
bigram_tagger = BigramTagger(train_data, backoff=unigram_tagger)
print(bigram_tagger.evaluate(test_data))
trigram_tagger = TrigramTagger(train_data,backoff=bigram_tagger)
print(trigram_tagger.evaluate(test_data))
# ===============================================================
title("Regex tagger")
from nltk.tag.sequential import RegexpTagger
regexp_tagger = RegexpTagger(

    [(r'^-?[0-9]+.([0-9]+)?$', 'CD'),   #cardinal numbers
     (r'(The|the|A|a|An|an)', 'AT'),    #articles
     (r'.*able$', 'JJ'),                #adjectives
     (r'.*ness$', 'NN'),                #nouns
     (r'.*ly$', 'RB'),                  #nouns formed from adjectives
     (r'.*ing$','VBG'),                 #geruns
     (r'.*ed$', 'VBD'),                 #past tense verbs
     (r'.*', 'NN'),                     #nouns (default)
    ])
print(regexp_tagger.evaluate(test_data))
# ===============================================================
title("Brill tagger")
print("Yet another one")
# ===============================================================
title("Machine learning based tagger")
print("There are some machine learning based algorithms")
print("NLP courses at : www.coursera.org/courses/nlp")
print("HMM coursrs at : http://mlg.eng.cam.ac.uk/zoubin/papers/ijrai.pdf")
print("MEX (Maximum Entropy Classifier) at : nlp.stanford.edu/software/tagger.shtml")
# ===============================================================
title("Named entity recognition")
print("NLTK as a NER Tagger")
from nltk import ne_chunk
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
sent = "Mark is studying at Stanford University in California"
print(ne_chunk(nltk.pos_tag(word_tokenize(text)),binary=False))
# ===============================================================
title("Standford NER")
sentence = text.split()
from nltk.tag.stanford import StanfordNERTagger
st = StanfordNERTagger('/Users/samuelmarticotte/nltk_data/classifiers/stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz',
                       '/Users/samuelmarticotte/nltk_data/classifiers/stanford-ner-2018-10-16/stanford-ner.jar')

list_of_tupples = st.tag(sentence)
print(list_of_tupples) #[('The', 'O'), ("city's", 'O'), ('landmarks', 'O')...]

for key,value in list_of_tupples:
    if value is not "O":
        print("{} : {}".format(key, value))

# ===============================================================
title("Specialized entity tagger")
print("code.google.com/p/python-calais/")
# ===============================================================
title("Tagging money and dates")
date_regex = RegexpTagger([(r'(\d{2})[/.-](\d{2})[/.-](\d{4})$','DATE'),(r'\$','MONEY')])
test_tokens = "I will be flying on sat 10-02-2014 with around 100M $ ".split()
print(date_regex.tag(test_tokens))

# print only MONEY and DATE
for key,value in date_regex.tag(test_tokens):
    if value is not None:
        print(key,value)
# ===============================================================

# ===============================================================


# ===============================================================


# ===============================================================


# ===============================================================


# ===============================================================


# ===============================================================

Banner("Good bye")