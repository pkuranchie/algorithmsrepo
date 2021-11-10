# User inputs two numbers. One number is assigned to a variable, the other number is assigned to another variable.
# The task is to invert the variables, so that the first variable contains the second neumber, while the first number
# is in the second variable


a = int(input('Input value a: '))
b = int(input('Input value b: '))

print(f'a = {a} and b = {b}')   # a = 10, b = 5

a = a + b   # 10 + 5 = 15; a = 15, b = 5
b = a - b   # 15 - 5 = 10; a = 15, b = 10
a = a - b   # 15 - 10 = 5; a = 5, b = 10

print(f'a = {a} and b = {b}')

# a = 5
# b = 7
#
# X = a
# a = b
# b = X

# a, b = b, a