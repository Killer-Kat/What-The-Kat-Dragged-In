@echo off
Rem this script uses the color command and a loop to create rainbow text
Rem use timeout >nul to pause without printing to the screen
title Rainbow
echo RAINBOWS FOR EVERYONE
echo RAINBOW TEXT!!!
echo HELLO WORLD!
rem this loop causes the text to cycle colors
rem it cycles text color by changing the text color but keeping the background black aka hex code "0"
rem “How much more black could this be?" and the answer is "None...none more black” ~ Spinal Tap
:loop
color 0C
timeout /t 1 /nobreak >nul
color 0E
timeout /t 1 /nobreak >nul
color 0a
timeout /t 1 /nobreak >nul
color 0b
timeout /t 1 /nobreak >nul
color 09
timeout /t 1 /nobreak >nul
color 0d
timeout /t 1 /nobreak >nul
goto loop
