# Given an array of integers. Calculate sum and multiplication of elements.
# Return the list, calculated sum, and multiplicaiton of elements
# Example: [1, 7, 3] Return: [11, 21]


def find_sum_and_mult(arr):
    sum_result = 0
    mult_result = 1
    for num in arr:
        sum_result = sum_result + num
        mult_result = mult_result * num
        
    return [sum_result, mult_result]

test_list = [1, 7, 3]
print(find_sum_and_mult(test_list))