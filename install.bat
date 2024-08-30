@echo off

echo Hello! Welcome to the installation of the IQ Test Game. Make sure that you are connected to the internet and you installed Python 3 from the official site.

echo Installing libraries...

python -m pip install -r requirements.txt

echo
echo Creating a shortcut.

set "target=%~dp0main.py"
set "icon=%~dp0logo.ico"
set "desktop=%UserProfile%\Desktop\IQ Test.lnk"
set "fallback=%~dp0IQ Test.lnk"
:: I need to create a shortcut NEAR the working directory, NOT in. (ERROR n1)

:: This part isn't the final version, but it's here because the next version has an error with "else", and idk why... (ERROR n2)

:: So, I'll delete this one :

if not exist "%desktop%" (
    powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%desktop%'); $s.TargetPath = '%target%'; $s.IconLocation = '%icon%'; $s.Save()" 2>nul
    echo A shortcut was created at the desktop.
)

if not exist "%desktop%" (
    echo To create a shortcut on the desktop isn't possible. Trying it near the directory.
    powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%fallback%'); $s.TargetPath = '%target%'; $s.IconLocation = '%icon%'; $s.Save()"
    echo A shortcut was created near the working directory.
)

:: When I debug this one:

::if not exist "%desktop%" (
::    powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%desktop%'); $s.TargetPath = '%target%'; $s.IconLocation = '%icon%'; $s.Save()" 2>nul
::    echo A shortcut was created at the desktop.
::)
::else (
::    echo A shortcut on the desktop already exists.
::)
::
::if not exist "%desktop%" and (
::    echo To create a shortcut on the desktop isn't possible. Trying it near the directory.
::    if not exist "%fallback%" (
::        powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%fallback%'); $s.TargetPath = '%target%'; $s.IconLocation = '%icon%'; $s.Save()"
::        echo A shortcut was created near the working directory.
::    )
::    else (
::        echo A shortcut near the directory already exists.
::    )
::)

echo Opening the game...

python main.py

echo Installation is finished. Enjoy!
