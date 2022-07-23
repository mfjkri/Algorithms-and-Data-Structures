import csv

data = [
    ["John", 20],
    ["Alice", 25],
    ["Charlie", 18]
]

with open("signups.csv", "w") as csv_file:
    myWriter = csv.writer(csv_file)

    # use the writerows method and pass in a 2D list to write multiple rows to a csv file
    myWriter.writerows(data)
