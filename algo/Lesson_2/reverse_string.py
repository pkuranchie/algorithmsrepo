# Given a string. Return a reversed string.
# abcde -> edcba

# O(n)
def reverse_str(s):
    reversed_string = '' # return s[::-1]

    index = len(s) -1
    while index >= 0:
        reversed_string = reversed_string + s[index]
        index -= 1

    return reversed_string



s = '12345'
print(s)
print(reverse_str(s))