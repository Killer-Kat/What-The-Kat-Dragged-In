@echo off
Rem This writes a visual basic script to the users startup folder so that it will execute when the user logs on
Rem the script shows an error message with a prompt to replace the user, just for the lols.

C:
cd %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
echo x=msgbox("User error: Please replace user.", 0+48, "USER ERROR") >> UserError.vbs
start UserError.vbs
