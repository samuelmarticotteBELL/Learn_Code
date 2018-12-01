#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# To compile: python ./name.py
# For libraries: pipenv install <package>
# pip install pyfiglet / conda install -c conda-forge pyfiglet
import sys, os
from pyfiglet import Figlet

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
Banner("Welcome to nltk")





Banner("Good bye")