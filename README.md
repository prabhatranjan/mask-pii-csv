# mask-pii-csv

# Update CSV File

This project contains a Python function that reads a CSV file, replaces some data based on a regex pattern, and saves the updated CSV file. It also includes shell and batch scripts that install Python and the necessary libraries and then call the Python function.

## Usage

To use this project, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Determine your operating system:
    * If you are using a Linux-based system or macOS, run the shell script by running the following command in the terminal: `./update_csv_file.sh`.
    * If you are using Windows, run the batch script by double-clicking on the `update_csv_file.bat` file in File Explorer or by running the following command in the Command Prompt: `update_csv_file.bat`.
4. Follow the prompts to input the necessary information to update the CSV file.
5. Once the script completes successfully, the updated CSV file will be saved to the specified output file path.

## Requirements

To use this project, you will need:

* Python 3
* pip (Python package installer)
* pandas (Python library)

## Installation

To install Python 3 and pip, follow these steps:

1. Linux-based systems: Python 3 and pip should already be installed. If they are not, you can install them using your package manager (`apt-get`, `yum`, etc.).
2. macOS: Python 3 should already be installed. If it is not, you can download and install it from the official website: https://www.python.org/downloads/mac-osx/.
3. Windows: Download and install Python 3 from the official website: https://www.python.org/downloads/windows/. Then, open the Command Prompt and run the following command to install pip: `python -m ensurepip --default-pip`. You may need to add Python to your system PATH variable.

To install the `pandas` library, open the Command Prompt (or terminal on Linux/macOS) and run the following command: `pip install pandas`.
