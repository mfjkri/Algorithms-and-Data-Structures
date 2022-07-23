import csv

with open('signups.csv', 'r') as csv_file:
    # use csv.reader function and pass in csv_file
    myReader = csv.reader(csv_file)

    # line count to skip first row of csv file
    lineCount = 0

    # iterate through myReader to extract each row as a list
    for row in myReader:
        if lineCount == 0:
            lineCount += 1
            continue
        print(row)
