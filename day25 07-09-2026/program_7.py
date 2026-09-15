from organized_project import greet, create_report


def main():
    print(greet("Arjun"))

    report = create_report()
    print("Products:", report["items"])
    print("Total price:", report["total_price"])


if __name__ == "__main__":
    main()
