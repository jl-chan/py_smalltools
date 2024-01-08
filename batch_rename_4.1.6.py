# Sample Name: PLNGUIFOS0A_10.123.124.125

import shutil, os
import csv

# Path to the parent directory
parent_directory=r"C:\Users\JiaLiang_Chan\Downloads\Web UI Screenshot"
csv_file =r"C:\Users\JiaLiang_Chan\Downloads\TestCase_4.1.6_lookup.csv"

# Initialize an empty lookup dictionary
lookup = {}

# Read from the CSV file and populate the lookup dictionary
with open(csv_file, 'r') as f:
    csv_reader = csv.DictReader(f,fieldnames=['hostname','IP'])
    for row in csv_reader:
        # Capitalize the hostname and remove any leading/trailing whitespaces
        hostname = row['hostname'].upper().strip()  # Capitalize the filename
        lookup[row['IP']] = hostname

# Extract all .tar.gz files to the parent directory
for filename in os.listdir(parent_directory):
    if filename.endswith('.png'):
        # Remove the extension (.png) from filename
        filename_no_ext = filename[:-4]
        # Check if the filename (in IP) matches any entry in the lookup
        if filename_no_ext not in lookup:
            print(f"IP: {filename_no_ext} is not available in the lookup. Re-check typo for the screenshot?")
        else:
            modified_file_name = f"{lookup[filename_no_ext]}_{filename}"
            shutil.move(os.path.join(parent_directory, filename), os.path.join(parent_directory, modified_file_name))
            print(f"Renamed {filename} to {modified_file_name}")