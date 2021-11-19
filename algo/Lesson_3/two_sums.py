# Given an array of integers nums and an integer target.
# Return two numbers from the array such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order


def pair_sum(arr, k):  # arr = [3, 7, 4, 9, 15, 3]; target number = 6
    if len(arr) < 2:
        return -1

    sum_set = set()

    for num in arr:
        target = k - num  # 6 - 3 = 3

        if target not in sum_set:
            sum_set.add(num)
        else:
            return [target, num]


test_arr = [3, 7, 4, 9, 15, 3]
test_target = 18
print(pair_sum(test_arr, test_target))  # [15, 3]
