import my_module


def main():
    name = input("Enter your name: ")
    print(my_module.welcome_user(name))

    numbers = [2, 4, 6, 8]
    squares = my_module.square_numbers(numbers)
    print(f"Squares of {numbers} are: {squares}")

    prices = [150, 220, 300]
    total = my_module.calculate_total(prices)
    print(f"Total price: {total}")


if __name__ == "__main__":
    main()

