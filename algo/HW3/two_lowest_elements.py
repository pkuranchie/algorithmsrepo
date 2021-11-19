# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2] Return: 2, 3


def find_two_lowest_elements(arr):
    arr.sort()
    return arr[:2]


list_to_test = [198, 3, 4, 9, 10, 9, 2]
print(list_to_test)
print(find_two_lowest_elements(list_to_test))