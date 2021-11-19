# Given an array of integers, return ture if the following conditions are fulfilled:
# - length of the array is bigger than or equal to 3
# - there exists some index i such that:
# a[0] < a[1] < ... <a[i]
# a[i] > a[i+1] > ... > a[a.size-1]
#
# Basically, find if there is an increasing subarray followed by a decreasing subarray
# [3, 5, 5] -> false
# [3, 4, 5, 2] -> true

# O(n)
def is_mountain(arr):
    i = 1

    while i < len(arr) and arr[i] > arr[i - 1]:
        i = i + 1

    if i == 1 or i == len(arr):
        return False

    while i < len(arr) and arr[i] < arr[i -1]:
        i = i + 1

    return i == len(arr)


test_arr_neg = [3, 5, 5] # -> false
test_arr_pos = [3, 4, 5, 2] # -> true

print(is_mountain(test_arr_pos)) # False
print(is_mountain(test_arr_neg)) # True