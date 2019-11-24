#!/bin/bash
#This is a test script to see if I can get user input and choose between several options

#this gets the users choice.
echo -n "Choose an option 1,2,3 : "
 read CHOICE
 echo "You chose : " $CHOICE

#This if tree displays the corresponding output
if [ $CHOICE = 1 ]
then 
   echo You chose one
elif [ $CHOICE = 2 ]
then 
   echo You chose two
elif [ $CHOICE = 3 ]
then
   echo You chose three
else 
   echo Invalid choice.
fi

