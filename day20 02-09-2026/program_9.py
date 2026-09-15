# WAP to create a custom exception
class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise CustomException("You must be 18 or older.")

    print("You are eligible.")
except CustomException as error:
    print("Custom error:", error)
except ValueError:
    print("Please enter a valid number.")
        
