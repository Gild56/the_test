@echo off

echo Hello! Welcome to the installation of the IQ Test Game. Make sure that you are connected to the internet and you installed Python 3 from the official site.

echo Installing libraries...

python -m pip install -r requirements.txt

echo Opening the game...

python main.py

echo Installation is finished. Enjoy!

pause
