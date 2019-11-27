@echo off
Rem Created by https://github.com/Killer-Kat
Rem This script writes a script to the users startup folder that logs them out every time they log on.
Rem Hilarious I know. 
Title Logged off initalizer
Color 0a
echo Hello, This script will write a second script to the currently logged on users startup folder
echo that will log them out everytime they log on.
echo Proceed with script? [Y]es [N]o [C]Lear Startup folder.
:errloop
set /p input=Select option. 
rem since unlike other languages batch doesnt have an else if function
rem I originally tried to do nested else (if) statments here but this method also works.
if /I "%input%"=="Y" ( goto CY)
if /I "%input%"=="N" ( goto CN )
if /I "%input%"=="secret" ( goto Secret )
if /I "%input%"=="C" ( goto CC 
) else (
echo error invalid selection.
goto errloop )
:CY
 cls
 echo input recived, Script proceeding.
 timeout /t 5
 cd %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
 echo @echo off > nope.bat
 echo title Nope >> nope.bat
 echo shutdown /l /f >> nope.bat
 echo Script Completed press any key to exit
 pause >nul
 exit /B
:CN
 cls
 color 0C
 echo Script terminated press any key to exit
 pause >nul
 exit /B

:CC
 cls
 rem this is just my startup folder cleaner script imported into this script.
 rem this script will delete any batch files from your user startup folder
 rem WARNING it does not discriminate if you have any .bat files in your startup folder you want to keep DO NOT run this script
 rem This script created by https://github.com/Killer-Kat for windows 10
 title Startup folder .bat remover
 color 0A
 echo Hello this script will delete all .bat files in the currently logged on users startup folder
 timeout /t -1
 cls
 color 0C
 title WARNING
 echo WARNING THIS SCRIPT DOES NOT DISCRIMINATE it will delete all .bat files from your startup folder if you do not want this to happen terminate the script instead of proceding.
 timeout /t -1
 cls
 title Startup folder .bat remover
 color 0A
 cd %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
 echo This is the contents of your startup directory.
 dir /b /oe /p
 timeout /t -1
 cls
 del *.bat
 echo Script completed
 echo This is the updated contents of your startup directory.
 dir /b /oe /p
 echo Press any key to exit
 pause >nul
 exit /B
:Secret
cls
echo illuminati confirmed
start https://www.youtube.com/watch?v=zwZISypgA9M
timeout /t 5 /nobreak >nul
echo    h::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::h
echo    y                                                                                                  y
echo    y                                                                                                  y
echo    y                                                                                                  y
echo    y                                                                                                  y
echo    y                                                .-                                                y
echo    y                                               .dN-                                               y
echo    y                                              .dmhm:                                              y
echo    y                                             .dms+dm-                                             y
echo    y                                            .dMo::/mm-                                            y 
echo    y                                           .dN+-...-hm-                                           y
echo    y                                          .hMs:::////mm-                                          y
echo    y                                         .hN+.```````.dm-                                         y
echo    y                                        `hMo----------:mm-                                        y
echo    y                                       `hNs:--...```...:dm-                                       y
echo    y                                      `hM+.`   .-``-: ..-dm-                                      y
echo    y                                     `yNs/:.  `//-`-: :osoNd.                                     y
echo    y                                    `hMo.---`.-.`:- --.``-/dd.                                    y
echo    y                                   `yMdyso+--+/-`::`:+soso -md.                                   y
echo    y                                  `yMmssoo+`````.--` .--`` .+md.                                  y
echo    y                                 `yMs:::/+//:::::-.` /o+`:s+ .md.                                 y
echo    y                                `yMdoo/:--:-.`.::-`...`   .` /hMd.                                y
echo    y                                yMd/:/s+/ss++sso+++o+++++/:-.`-sNd`                               y
echo    y                              `sMMysmNNo+s/+/-`  -:-..:yh::////dMMd.                              y
echo    y                              sMMMNhy/:/-                  .:++osdMd`                             y
echo    y                             sMMMNy+.`  .``.-:::::::-```-.   `:++shMd`                            y
echo    y                            sMmm/:oyyy+++/:-.`-:- `:+++oyo/:/os:.:ymMd`                           y
echo    y                           sMmo+/syo+/.       ```   `./+oo+o+++oso/:hMd`                          y
echo    y                          oMh-++ys:`         `````     .::///+o+:/o+omMh`                         y
echo    y                         oMMNNho-   `.:/oshdmmNNNmmdhyo+/:+o+-./y+sdyhoNh`                        y
echo    y                        oMMNNmo`-/sdNNMMMNooodMMMMMMydmNNNdo/os:.yd-/mhhNh`                       y
echo    y                       oMh+:.`.+dNm/:NMNmd`  /ssmMMM.s:sm+odmy+oy:/dys++NMh`                      y
echo    y                      oMd:``:odNM/o+ smm:ys`  `sMMMh`y`so:o+:mNhomdNy+y+hNMh`                     y
echo    y                     +Nd: omNMMMdo`h`.yyy/+ys+sdMMN-:s`h. :o-dMMMMs+s+ooy+oMh`                    y
echo    y                    +Mdyo`hNMMMm+y./s `+s+ossyys+-.:y`+s `+` hhdMN++hs/:odhhNh`                   y
echo    y                   +Md/`o+:-/yd++./`+:`/+o//++//:/so:os` :. +smmyoys/h+os/--oMy`                  y
echo    y                  +NNd/`./o+/ ` ` `. :+..-/+++///+oo/.  `` `-.:hhdo++s//osso/oNy`                 y
echo    y                 +Nm-/ydds:`:.     `` ``   ``..````      `.-/osos+oo:+-:++--/sMMy`                y
echo    y                +NNhs+:om+-.:. -/. .:`-/:---..`````..-:/oys:-ss+`-::.`//+sosdo:/Ny`               y
echo    y               /NM/`:yo/::+. ..````--.+:-::/+//++:/+///-/+/``.--://:.:o:```-+hs+dMy`              y
echo    y              /NNddo++y/-:-``..` //`-:/:--.-/:-//.:////:://+/:-....-:/shsys+/::/hNMy`             y
echo    y             /NMd:-sd-` `-:-+/ `-. .:///////::::::::::/::::/+oooo+/:o+-` ./ss/..-oNMy`            y
echo    y            /NNsh.`oyhh:  `..` .-.`:/++//+++ooooooo+++ooo+//:--. ..-/yhooso+oosyo/:+Ns`           y
echo    y           /NNs+-:ho `o+ `./+.`/:  ``::`-+.`//` .+  `/. /+//+++:`///:-..-++:---:oyoodMs`          y
echo    y          /NMMd+/+hh++ys/dh/oyo++/+s////++//++//++/////+++o+//++++////shdy++oo++++sNMMMs`         y
echo    y         .osssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss.         y
echo    y                                                                                                  y
echo    y                                                                                                  y
echo    y                                                                                                  y
echo    y                                                                                                  y
echo    h::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::h
timeout /t 25 /nobreak >nul
echo Press any key to exit
pause >nul
exit /B