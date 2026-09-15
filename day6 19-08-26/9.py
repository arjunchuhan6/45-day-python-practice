#wap to create a countdown from a given number to zero using while loop but takes times to every countdown number 1sec for each countdown number
import time 

n = int(input("Enter a number: "))
while n >= 0:
    print(n)
    time.sleep(1)  # Pause for 1 second
    n -= 1
