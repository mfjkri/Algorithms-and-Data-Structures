import csv
import sys

if len(sys.argv) < 2:
    print("require file name")
else:
    with open(sys.argv[1], 'r') as csv_file:
        myReader = csv.reader(csv_file)
        for row in myReader:
            print(row)
