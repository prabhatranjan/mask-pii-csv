@echo off

REM Install Python 3 and pip
choco install -y python

REM Install necessary libraries
pip install pandas

REM Call the update_csv_file function
python update_csv_file.py
