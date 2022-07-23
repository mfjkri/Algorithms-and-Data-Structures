import csv

signups = []

with open('signups.csv', 'w') as csv_file:

    # csv.writer creates an object which allows us to write to csv files
    myWriter = csv.writer(csv_file)

    for i in range(3):
        name = input("name: ")
        age = input("age: ")

        # use the writerow method to write to a csv file
        myWriter.writerow([name, age])
