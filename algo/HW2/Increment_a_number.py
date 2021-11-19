# Write a program that takes as input an array of digits encoding
# a nonnegative decimal integer D and updates the array to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].


def uni_char(s):
    return len(set(s)) == len(s)


pos_test_str = 'abcde'
neg_test_str = 'abcdde'

print(uni_char(pos_test_str))
print(uni_char(neg_test_str))