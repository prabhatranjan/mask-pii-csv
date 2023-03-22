#!/bin/bash

# Install Python 3 and pip
apt-get update
apt-get install -y python3 python3-pip

# Install necessary libraries
pip3 install pandas

# Call the update_csv_file function
python3 update_csv_file.py
