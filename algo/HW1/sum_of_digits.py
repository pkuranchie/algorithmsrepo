# Compute the sum of digits in all numbers from 1 to n.
# When a user enters a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15


sum = int(input('Enter number:'))

if sum > 0:
    result = int(sum * ((sum + 1) / 2))
    print(f'Sum of 1 to {sum} is {result} ')
else:
    print(f'You have entered an negative number. Enter a positive number')


