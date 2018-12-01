#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# To compile: python ./name.py
import sys, os
from tkinter import *
from tkinter import messagebox
import subprocess

#####------------------------------------------------(Constants)
#arguments=
#name=
#path=
#version=1.0 
program_name="template"

def sep(): #print a separator line
	print('---------------------------------------')
	
def welcome():
	print('\033[1;31m***********************************\033[1;m')
	print('\033[1;31m*******Welcome to my program*******\033[1;m')
	print('\033[1;31m***********************************\033[1;m\n')
	print('Usage: program [option]')	

def goodbye():
	print('\033[1;34m***********************************\033[1;m')
	print('\033[1;34m*************GOOD BYE**************\033[1;m')
	print('\033[1;34m***********************************\033[1;m')
	exit()
	
def zero():
	window.destroy()
	goodbye()
	
def one():
	#call a system process and pipes it to variable results_message
	results_message = subprocess.Popen(["ls"], stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0]
	results.delete("1.0", END)
	results.insert("1.0", "Files in current directory :\n\n")
	results.tag_add("start", "1.0", "1.30")
	results.tag_config("start", background="black", foreground="purple")
	return

def two():
	print("Hello from two")
	"""
	results.delete("1.0", END)
	results.insert("1.0", "This functions has called samba on 192.168.0.101\n\n")
	os.system('open smb://192.168.0.101')
	"""
	return
	
def three():
	print("Hello from three")
	return

def four():
	print("Hello from four")
	return
	
def five():
	print("Hello from five")
	return
	
def six():
	print("Hello from 6 ")
	return

def seven():
	print("Hello from 7")
	return
	
def eight():
	print("Hello from 8")
	return
	
def nine():
	print("Hello from 9")
	return
	
def ten():
	print("Hello from 10")
	return

def printmenu():
	a = """
	PROGRAM MENU: 
	
		1- Not implemented
		2- Not implemented
		3- Not implemented
		4- Not implemented
		5- Not implemented
		6- Not implemented
		7- Not implemented
		8- Not implemented
		9- Not implemented
		10-Not implemented
		
		0-Exit
	"""
	print(a)
	
####GUI PROGRAMMING-----------------------------------(GUI ELEMENTS)
#This creates the window object
window = Tk()
#Size of window
window.geometry("800x600")
window.title("Welcome to " + program_name)
#-----------------------Text--------------------------
#Welcome Message
welcome = Text(window)
welcome.insert(INSERT, "Welcome to " + program_name)
welcome.place(bordermode=OUTSIDE, height=50, width=600)

results = Text(window)
results.insert(INSERT, "Program results : " )
results.place(bordermode=INSIDE, x=150, y=50)


#-----------------------Text End----------------------

#-----------------------Buttons-----------------------
#Size of window

#Button one
B1 = Button(window, text = "Function 1", command = one)
#Location of button in window
B1.place(x = 0, y = 50)

#Button two
B2 = Button(window, text = "Function 2", command = two)
#Location of button in window
B2.place(x = 0, y = 80)

#Button three
B3 = Button(window, text = "Function 3", command = three)
#Location of button in window
B3.place(x = 0, y = 110)

#Button four
B4 = Button(window, text = "Function 4", command = four)
#Location of button in window
B4.place(x = 0, y = 140)

#Button five
B5 = Button(window, text = "Function 5", command = five)
#Location of button in window
B5.place(x = 0, y = 170)

#Button six
B5 = Button(window, text = "Function 6", command = six)
#Location of button in window
B5.place(x = 0, y = 200)

#Button seven
B6 = Button(window, text = "Function 7", command = seven)
#Location of button in window
B6.place(x = 0, y = 230)

#Button eight
B7 = Button(window, text = "Function 8", command = eight)
#Location of button in window
B7.place(x = 0, y = 260)

#Button nine
B8 = Button(window, text = "Function 9", command = nine)
#Location of button in window
B8.place(x = 0, y = 290)

#Button ten
B9 = Button(window, text = "Function 10", command = ten)
#Location of button in window
B9.place(x = 0, y = 320)

#Button quit
B10 = Button(window, text = "Quit program", bg = "red", command = zero)
#Location of button in window
B10.place(x = 0, y = 500)

#-----------------------Buttons end--------------------

####GUI PROGRAMMING------------------------------(END GUI ELEMENTS)

#### Main ----------------------------------------(Main)
#This keeps alive window-----------------
window.mainloop()
