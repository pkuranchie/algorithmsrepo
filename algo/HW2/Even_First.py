# Your input is an array of integers, and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input array).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def split_in_half(s):
    length = len(s)
    half = length // 2
    add = 0
    if length % 2:
        add = 1

    left = s[:half + add]
    right = s[half + add:]

    print(left)
    print(right)

    return right + left

test_str = 'bbbbbcaaaaa'
print(split_in_half(test_str))