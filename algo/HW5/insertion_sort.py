# O(n^2)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

    print(f'Original Sort: {arr}')
    return f'Descending Order: {arr[::-1]}'


test_list = [4, 7, 3, 9, 10, 2, 6, 11]
print(test_list)
print(insertion_sort(test_list))