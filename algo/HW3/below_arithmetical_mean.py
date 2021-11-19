# When given a list, the program should return a list of all the elements below the original list's arithmetical mean.
# The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3](The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]


def below_ar_mean(arr):
    ar_mean = sum(arr) / len(arr)
    print(f'Ar. mean: {ar_mean}')
    final_list = []
    for num in arr:
        if num < ar_mean:
            final_list.append(num)
    return final_list
    
    
list_to_test = [1, 3, 5, 6, 4, 10, 2, 3]
print(list_to_test)
print(below_ar_mean(list_to_test))