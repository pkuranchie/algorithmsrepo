# Write a program that takes as input an array of digits encoding a nonnegative decimal integer D and updates
# the array to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

# O(n)
def plus_one(arr):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        print(i)
        print(arr)
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i -1] += 1

    print(arr)
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)

    return arr


test_list_1 = [1, 2, 7]
test_list_2 = [1, 2, 9]
test_list_3 = [9, 9, 9]

# print(test_list_1)
# print(plus_one(test_list_1))
#
# print(test_list_2)
# print(plus_one(test_list_2))

print(test_list_3)
print(plus_one(test_list_3))