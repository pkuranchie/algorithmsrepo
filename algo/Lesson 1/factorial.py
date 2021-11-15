# When User enters a number, its factorial is displayed


import math

number = int(input('Input your number:'))

factorial = 1
if number != 0:
    for n in range(1, number + 1):
        factorial = factorial * n # factorial *= n


# factorial = math.factorial(number)

print(f'The factorial of {number} is {factorial}')