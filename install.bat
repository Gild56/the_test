@echo off

echo Hello! Welcome to the installation of The Test Game.
echo Make sure that you are connected to the internet and have installed Python 3 from the official site.

echo Installing libraries...

python -m pip install -r requirements.txt

echo
echo Creating a shortcut...

set "target=%~dp0main.py"
set "icon=%~dp0logo.ico"
set "desktop=%UserProfile%\Desktop\The Test.lnk"
set "fallback=%~dp0..\The Test.lnk"  :: Creates a shortcut one directory above the working directory

if not exist "%desktop%" (
    powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%desktop%'); $s.TargetPath = '%target%'; $s.IconLocation = '%icon%'; $s.Save()"
    if errorlevel 1 (
        echo Failed to create shortcut on the desktop. Trying to create it near the directory.
    ) else (
        echo A shortcut was created on the desktop.
    )
)

if not exist "%desktop%" (
    powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%fallback%'); $s.TargetPath = '%target%'; $s.IconLocation = '%icon%'; $s.Save()"
    if errorlevel 1 (
        echo Failed to create the shortcut near the directory.
    ) else (
        echo A shortcut was created near the working directory.
    )
)

echo Opening the game...

python main.py

echo Installation is finished. Enjoy!
