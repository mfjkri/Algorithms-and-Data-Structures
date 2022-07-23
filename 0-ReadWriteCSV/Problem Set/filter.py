'''
    Filter
        1. Take in a csv file name as a command line argument 
           (signups1.csv, signups2.csv or signups3.csv)
        2. Read from that csv file name using the csv module
        3. Print out the names of signups with age > 18 from the data read
'''

import sys
import csv


with open(sys.argv[1], 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    for row in csv_reader:
        name: str
        age: str

        name, age = row
        if int(age) > 18:
            print(name)
