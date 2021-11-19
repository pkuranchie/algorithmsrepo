# Find a sum of elements between min and max elements.
# Min and max elements are not included.
# All numbers are unique


# [1, 5, 3, 7, -3, 4, 10]
# min_value = -3, min_index = 4
# max_value = 10, max_index = 6
# sum = 4


# [19, 5, 3, 7, -3, 4, 10]
# min_value = -3, min_index = 4
# max_value = 19, max_index = 6
# sum = 15


def sum_between_min_and_max(arr):
    if len(arr) <= 2:
        return -1
    
    min_value = max_value = arr[0]
    min_index = max_index = i = 0
    
    while i < len(arr):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i
        i = i + 1
        
    return sum(arr[min(min_index, max_index) + 1:max(min_index, max_index)])


test_list_minmax = [3, 1, 5, 6, 7, 2, 19, 8] # 20
test_list_maxmin = [3, 19, 5, 6, 7, 2, 1, 8] # 20

print(test_list_minmax)
print(sum_between_min_and_max((test_list_minmax)))

print(test_list_maxmin)
print(sum_between_min_and_max(test_list_maxmin))