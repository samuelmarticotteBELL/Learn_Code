
#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# To compile: python ./name.py
# For libraries: pipenv install <package>
# pip install pyfiglet / conda install -c conda-forge pyfiglet
import sys, os
from pyfiglet import Figlet #banners
import re                   #regulare expressions
import urllib3
import requests
import nltk
from nltk.corpus import stopwords
set(stopwords.words('english'))
from bs4 import BeautifulSoup
import string
from wordcloud import WordCloud
import csv

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
Banner("Welcome to Wordle")
#===============================================================
title("Print how many lines of html")
url = 'https://en.wikipedia.org/wiki/List_of_Warriors_characters'
language = 'english'
#url = 'http://192.168.2.11/'
with requests.get(url) as response:                 #request url
    html = response.content
    print("This website ({}) has {} lines of text\n".format(url, len(html)))

    #tokens = [tok for tok in html.split()]         #get all tokens from response

    raw = BeautifulSoup(html, features='lxml').get_text() #get html from url response and remove taks
    almost_tokens = nltk.wordpunct_tokenize(raw)                       #tokenize html input

    #remove punctuation
    tokens = [x for x in almost_tokens if not re.fullmatch('[' + string.punctuation + ']+', x)]

    #remove stopwords
    filtered_word_list = tokens[:]                  #make a copy of the list
    for word in tokens:                             #for all tokens
        if word in stopwords.words(language):      #for word in list is a stop wor
            filtered_word_list.remove(word)         #remove stopwords from list of words

    #sort words inversely
    print("Total numer of tokens: {}".format(str(len(tokens))))
    Freq_dist_nltk=nltk.FreqDist(filtered_word_list) #calculate the frequency of every token
    i=0
    for key,value in sorted(Freq_dist_nltk.items(),reverse=True,key=lambda item: (item[1], item[0])): #sort words by frequency inversely
            print("{}: {}".format(key,value))
            i=i+1
            if i == 50: #break after
                break
#===============================================================
title("Plot frequency of words")
#Freq_dist_nltk.plot(60, cumulative=False)   #plot a graph
#===============================================================
title("Write result to csv")
with open('./output/words.txt', 'w') as file:
    wr = csv.writer(file, quoting=csv.QUOTE_ALL)
    wr.writerow(Freq_dist_nltk)

#===============================================================
title("Read from csv")
#read from csv
list_keys = []
with open('./output/words.txt', 'r') as f:
    reader = csv.reader(f)
    list_keys = list(reader)

#===============================================================
title('generate a wordcloud')
#print word cloud
wordcloud = WordCloud().generate(str(list_keys[0]))
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
wordcloud= WordCloud(max_font_size=40).generate(str(list_keys[0]))
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

#===============================================================
Banner("Good bye")