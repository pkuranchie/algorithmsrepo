# Give na list of random numbers.
# Find and return the max element and the index of this element
# Example: [1, 45, 33, 76, 9, 10] print [3, 76]


def find_max_element(arr):
    max_index = 0
    max_value = arr[max_index]

    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_index = i
            max_value = arr[i]

    return [max_index, max_value]


test_list = [1, 45, 33, 76, 9, 10]
print(test_list)
print(find_max_element(test_list))  # [0, 1]
