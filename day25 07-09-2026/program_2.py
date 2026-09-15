# import random module
import random

#generate random string of length 8
def random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
print("Random string of length 8 is:", random_string(8))