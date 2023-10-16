"""
        Mesclar Arrays
"""

def merge_array(array_1, array_2):
    array_merge = array_1 + array_2
    array_merge_sorted = sorted(array_merge)
    return array_merge_sorted


print(merge_array([1, 2, 3], [4, 5, 6]))
print(merge_array([1, 2, 3], [4, 5]))
print(merge_array([1, 2, 3], [4, 6, 7, 8]))
print(merge_array([1, 2, 2, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))