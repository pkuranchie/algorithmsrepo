# Given a string, write a python function to check if it is palindrone or not.
# A string is said to be palindrome if the reverse of the string is the same as string.
# For example, "radar" is a palindrome, but "radix" is not a palindrome.

def is_palindrome(s):
    return s == s[::-1]

str_pos = 'radar'
str_neg = 'radax'

print(is_palindrome(str_pos)) # True
print(is_palindrome(str_neg)) # False