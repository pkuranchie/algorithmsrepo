# Write a programe that takes an input a sorted array and updates itso that all duplicates
# have been removed and the remaining elements have been shifted left ot fill the emptied indices.
# Return the number of valid elements.
# Your cannot use sets for this coding challenge.


# [1, 2, 4, 4, 5, 6, 7, 10, 10, 18, 21, 21, 22] length = 13
# [1, 2, 4, 5, 6, 7, 10, 18, 21, 22, 0, 0, 0] length = 13


# O(N)
def delete_duplicates(arr):
    write_index = 1

    if len(arr) == 1:
        return 1

    for i in range(1, len(arr)):
        if arr[write_index - 1] != arr[i]:
            arr[write_index] = arr[i]
            write_index = write_index + 1

    for i in range(write_index, len(arr)):
        arr[i] = 0

    print(arr)
    return write_index


test_list = [1, 2, 4, 4, 5, 6, 7, 10, 10, 18, 21, 21, 22]
print(test_list)
print(delete_duplicates(test_list))
