def merge_arrays(arr1, arr2):
    result_arr = arr1 + arr2
    return sorted(result_arr)

print(merge_arrays([12, 14, 16], [11, 13, 17]))
print(merge_arrays([22, 24, 26, 28], [21, 27]))