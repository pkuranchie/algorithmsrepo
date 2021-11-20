# O(n^2)

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    print(f'Original Sort: {arr}')
    return f'Descending Order: {arr[::-1]}'


test_list = [2, 7, 6, 1, 10, 5, 4, 8]
print(test_list)
print(selection_sort(test_list))
