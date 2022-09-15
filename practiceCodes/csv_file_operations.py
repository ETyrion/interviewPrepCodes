import csv

with open('sample_csv.csv') as sample_csv_reader:
    reader = csv.reader(sample_csv_reader)
    for row in reader:
        print(row[1])