'''
    Signup
        1. Ask the user for three signups
            - Each signup should consist of a name and age
        2. Write the signups to a file called signups4.csv
        3. The first row of the csv file should be the name of the columns (Name,Age)
'''

import csv


def get_integral_input(input_label: str, input_prompt: str = "") -> int:
    user_input: int

    while True:
        try:
            user_input = int(input(input_prompt))
            break
        except ValueError:
            print(
                f"You have entered an invalid {input_label}.")

    return user_input


sign_ups = []

for i in range(0, 3):
    name = input("Please enter your name:")
    age = get_integral_input(
        input_label="age",
        input_prompt="Please enter your age:"
    )
    sign_ups.append([name, age])

with open("signups4.csv", 'w', newline='') as sign_up_csv_file:
    csv_writer = csv.writer(sign_up_csv_file, delimiter=',')

    csv_writer.writerow(["Name", "Age"])

    [csv_writer.writerow(row) for row in sign_ups]
