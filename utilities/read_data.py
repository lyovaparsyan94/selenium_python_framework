import csv


def get_csv_data(file_name):
    rows = []
    # Create an empty list to store rows
    data_file = open(file_name, "r")
    # Open the CSV file Reader from CSV file
    reader = csv.reader(data_file)
    # Skip the headers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows