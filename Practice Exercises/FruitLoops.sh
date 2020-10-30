#!/bin/bash
#This is a simple script with a loop that just prints random fruits.
echo A part of this balanced breakfast:
while [ 1=1 ]; do
RAND=$((RANDOM%10))
if [ $RAND = 1 ]
then
 echo Apple
elif [ $RAND = 2 ]
then
 echo Banana
elif [ $RAND = 3 ]
then
 echo Mango
elif [ $RAND = 4 ]
then
 echo Guava
elif [ $RAND = 5 ]
then
 echo Orange
elif [ $RAND = 6 ]
then
 echo Strawberry
elif [ $RAND = 7 ]
then
 echo Kiwi
elif [ $RAND = 8 ]
then
 echo Blueberry
elif [ $RAND = 9 ]
then
 echo Tomato
elif [ $RAND = 10 ]
then
 echo Papaya
else
 echo Raspberry Pi
fi
sleep 1
done
