# Imports the csv module

import csv

# Create a CSV file
# This defines a list called csv_data that represents the data to be written to the CSV file.

csv_data = [
    ['1', 'Sarah', 'Kichou', 'Algeria'],
    ['2', 'Alba', 'Torres', 'Spain'],
    ['3', 'Reyes', 'Rodriguez', 'Spain']
]

# This sets the name of the CSV file we want to create.
csv_file = 'data.csv'

# This block of code opens the CSV file (data.csv) in write mode,
# prepares a CSV writer object to write to the file, writes the header row
# (id, name, surname, country),
# and then writes each row of data from csv_data to the file.
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'name', 'surname', 'country'])
    writer.writerows(csv_data)

print("Here We create the CVS")

# Read the CSV file
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    # Converts the reader object into a list called data that
    # contains the rows of data from the CSV file.
    data = list(reader)

# Process the data and add a new column
data[0].append('full_name')

# This loop iterates over each row (excluding the header row) in data
# and creates a new column called full_name by
# combining the values of the name and surname columns.
for row in data[1:]:
    # Concatenate name and surname
    full_name = row[1] + ' ' + row[2]
    row.append(full_name)

# This loop iterates over each row in data and prints it.
for row in data:
    print(row)
