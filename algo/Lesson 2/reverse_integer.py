# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

# 123 => 321

# 0(1)
def reverse_int(n):
    s = str(n)

    if s[0] == '-':
        return int('-' + s[:0:-1])
    return int(s[::-1])


print(reverse_int(123))
print(reverse_int(-456))