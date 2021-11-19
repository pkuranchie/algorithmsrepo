# Given an array of integers, write a function to move all 0's to the end
# while maintaining the relative order of the other elements.
# 0 4 0 3 12 -> 4 3 12 0 0


def move_zeros(arr):
    i = 0

    for num in arr:
        if num != 0:
            arr[i] = num
            i = i + 1

    # i = 3
    # 0 4 0 3 12
    # 4 3 12 3 12

    while i < len(arr):
        arr[i] = 0
        i = i + 1

    # i = 5
    # 0 4 0 3 12
    # 4 3 12 0 0

    return arr


test_list = [0, 4, 0, 3, 12]
print(move_zeros(test_list))
