# Consider an array of non-negative integers.
# A second array is formed by shuffling the elements of the first array and deleting a random element.
# Given these two arrays, find which element is missing in the second array
# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
# Input:
# [1,2,3,4,5,6,7], [3,7,2,1,4,6]
#
# Output:
# 5 is the missing number

# [2,1,3,4,7,6,5]
# [3,7,2,1,4,6]

# Step 1. Sort arrays.
# [1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 6, 7]

# Step 2. Compare 2 arrays index by index.

# O(N*logN)
# def find_missing_number(list1, list2):
#     list1.sort()
#     list2.sort()
#
#     for num1, num2 in zip(list1, list2):
#         if num1 != num2:
#             return num1
#
#
# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = [1, 2, 3, 4, 6, 7]
# print(find_missing_number(list1, list2))

# O(N*logN)
import collections


def find_missing_number(list1, list2):
    dlist = collections.defaultdict(int)

    for num in list2:
        dlist[num] += 1

    for num in list1:
        if dlist[num] == 0:
            return num
        else:
            dlist[num] -= 1


list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [1, 2, 3, 4, 6, 7]
print(find_missing_number(list1, list2))
