'''
    Hello
        1. Ask the user for his name
        2. Ask the user for his age
        3. Print "Hello <name>, <age>"
'''


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


def main():
    name = input("Please enter your name:")
    age = get_integral_input(
        input_label="age",
        input_prompt="Please enter your age:"
    )

    print(
        f"Hello {name}, {age}"
    )


if __name__ == "__main__":
    main()
