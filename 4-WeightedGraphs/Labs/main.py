
def square_root(x: float, precision: float = 0.01) -> float:
    y: float = float(x / 2)

    while True:
        new_y = (y + (x / y)) / 2

        diff = abs(y - new_y)
        y = new_y

        if diff < precision:
            return y


def get_number(prompt_msg: str) -> float:
    while True:
        num: float

        try:
            num = float(input(prompt_msg))
            return num
        except ValueError:
            print("You have entered an invalid number. Please try again.")


def main() -> None:
    precision: float = get_number("Enter your precision: ")
    print()

    while True:
        x: float = get_number("Enter a number: ")

        if x > 0:
            result = square_root(
                x=x,
                precision=precision
            )
            print(f"The root of {x} is {result}.\n")
        else:
            print("Unfortunately we only accept positive values.")


if __name__ == "__main__":
    main()
