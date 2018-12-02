#!/bin/bash

#GOAL : GOAL OF THE PROGRAM

#####------------------------------------------------(Constants)

PROG_NAME= #Program name
PROG_PATH=$0
VERSION=1.0 #Version and revision

#Welcome message function------------------------------(Welcome)
welcome_message(){
clear
echo "******************************************************"
echo "******Welcome to my $PROG_NAME program $VERSION***********"
echo "******************************************************"
echo "usage: $0 [#] "
} #End of welcome function

# Good bye message function----------------------------(Good bye)
good_bye() {
echo "******************************************************"
echo "**********************GOOD BYE!***********************"
echo "******************************************************"
exit 0;
} #End of good bye message

#-------------------------------------------------(Error message)
# Error handling: contains one argument: string with error message
error_exit() {
# Display error message and exit
echo "Error: "; echo "${1:-"Unknown Error"}" 1>&2
press_enter
}
#End of Error exit

#--------------------------------------------------(Press enter)
#Clearscreen: Ask to press enter and clears the screen
press_enter(){
echo -en "\nPress Enter to continue"
read
}
#End of clearscreen

#----------------------------------------------------------(1)
function_1(){
echo "function1 not yet implemented"
}

#----------------------------------------------------------(2)
function_2(){
echo "function2 not yet implemented"
}

#----------------------------------------------------------(3)
function_3(){
echo "function3 not yet implemented"
}
#----------------------------------------------------------(4)
function_4(){
echo "function4 not yet implemented"
}

#----------------------------------------------------------(5)
function_5(){
echo "function 5 is a test function"
#Error catching function
if  [ $? != 0 ]; then
	echo "Error unloading $another_deamon"
else
	echo "Succeeded in unloading: $PLIST"
fi
}

#------------------------------------------------(Menu of options)
printmenu(){
echo "
PROGRAM MENU: Choose an option
1-Function1
2-Function2
3-Function3
4-Function4
5-Test_Function

0-Exit program
"
}

#### Main menu----------------------------------------(Main Menu)
#Show welcome message
welcome_message
printmenu
#------------------------------------(Argument passed to the function)
optionPassed="false"
number_functions="5"
if [ "$#" == "1" ]; then
	if [[ $1 =~ -?[0-9]+ ]]; then #is a number
		if [ "$1" -ge 5  ]; then #is bigger than number of functions
     		optionPassed="false"
     		echo "Argument is bigger than $number_functions"
     	else
     		optionPassed="true"
     		echo "Argument passed is : $1"
    	fi
    else
    	optionPassed="false"
    	#echo "Argument is not a number"
	fi
elif [ "$#" == "0" ]; then #no argument passed
	optionPassed="false"
else					 #echo "Issue with arguments"
	optionPassed="false"
	
fi

#infinite loop
until [ "$selection" ==  "0" ]; do
if [ $optionPassed == "true" ]; then 
	echo "Argument passed is : $1"
	selection=$1
	optionPassed="false"
else #no argument was passed
	echo -n "Enter selection: " 
  	read selection
fi

case $selection in
#Call various programs------------------------------(Function calls)
1 ) function_1 ;;
2 ) function_2 ;;
3 ) function_3 ;;
4 ) function_4 ;;
5 ) function_5 ;;

#Option to leave the program------------------------------(Exit)
0 ) good_bye ;;
* ) clear; 
	printmenu;
	echo "Please enter a number between 0 and 4";
	
esac
if [ $optionPassed == "true" ]; then
	exit
fi
done
