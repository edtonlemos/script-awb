import os
import glob
import csv

# Define the directory to search for .xml files
directory = "path/to/your/directory"

# Find all .xml files in the specified directory
xml_files = glob.glob(os.path.join(directory, "*.xml"))

# Initialize counter and list for files containing the target text
counter = 0
files_with_text = []

# Loop through each .xml file
for file_path in xml_files:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Check if the target text is in the file's content
        if "ibpj_infra_awb" in content:
            counter += 1
            files_with_text.append(os.path.basename(file_path))

# Write the results to a .csv file
with open('result.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['File Name'])
    for file_name in files_with_text:
        csvwriter.writerow([file_name])
    # Write the total count at the end
    csvwriter.writerow(['Total', counter])