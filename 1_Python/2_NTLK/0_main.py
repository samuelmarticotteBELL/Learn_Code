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

#corpus in ~/nltk_data

#####------------------------------------------------(Constants)
#arguments=
#name=
#path=
#version=1.0 

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
def main():

	Banner("Welcome to nltk")
    
if __name__ == '__main__':
    main()

#===============================================================
Banner("Good bye")