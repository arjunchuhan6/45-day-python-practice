from my_package import greet_user, add, multiply


def main():
    name = input("Enter your name: ")
    print(greet_user(name))
    print("Addition:", add(10, 5))
    print("Multiplication:", multiply(10, 5))


if __name__ == "__main__":
    main()
