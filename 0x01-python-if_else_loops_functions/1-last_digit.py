#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Convert the number to a string
number_str = str(number)
last_digit = number_str
#Get the last digit of the number
last_digit = abs(number) % 10

if number < 0:
    last_digit = "-" + last_digit
# Print the output directly with a new line
print(f"Last digit of {number_str} is {last_digit} and is", end=" ")

if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print(f"less than 6 and not 0")
