import csv
import re
import sys

def update_csv_file(input_file_path, output_file_path, regex_pattern, replacement):
    # Open the input CSV file and read its contents
    with open(input_file_path, 'r') as input_file:
        csv_reader = csv.reader(input_file)
        rows = [row for row in csv_reader]

    # Use regex to replace data in each row
    updated_rows = []
    for row in rows:
        updated_row = []
        for item in row:
            updated_item = re.sub(regex_pattern, replacement, item)
            updated_row.append(updated_item)
        updated_rows.append(updated_row)

    # Write the updated rows to the output CSV file
    with open(output_file_path, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        for row in updated_rows:
            csv_writer.writerow(row)

if __name__ == '__main__':
    # Collect input from the user
    input_file_path = input("Enter path to input CSV file: ")
    output_file_path = input("Enter path to output CSV file: ")
    regex_pattern = input("Enter regex pattern: ")
    replacement = input("Enter replacement string: ")

    # Call the update_csv_file function with user input
    update_csv_file(input_file_path, output_file_path, regex_pattern, replacement)

    print(f"CSV file updated successfully and saved to {output_file_path}")
