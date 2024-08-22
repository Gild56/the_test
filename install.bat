@echo off

echo Hello! Welcome to the installation of the IQ Test Game. Make sure that you are connected to the internet.

cd /d "%~dp0"

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed on your system. Opening local python.exe...
    python.exe --version >nul 2>&1
)

echo Python is installed. Proceeding with installation...

echo Installing libraries...

python -m pip install pygame
python -m pip install kivy
python -m pip install colorama

echo Opening the game...

python main.py

echo Installation is finished. Enjoy!

pause
