def merge_two_arrays(arr1, arr2):
    i = j = 0
    n, m = len(arr1), len(arr2)
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            yield arr1[i]
            i += 1
        else:
            yield arr2[j]
            j += 1
    while i < n:
        yield arr1[i]
        i += 1
    while j < m:
        yield arr2[j]
        j += 1

merged_list = list(merge_two_arrays([2, 4], [2, 4, 5, 6, 71]))
print(merged_list)


def merge_two_arrays1(arr1, arr2):
    i   = j  = 0
    n , m = len(arr1), len(arr2)
    result  = []
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    while i < n:
        result.append(arr1[i])
        i+=1
    while j < m:
        result.append(arr2[j])
        j+=1
    return result
# def merge( nums1, m, nums2, n):
#     i = j = 0
#
# print(merge([1,2,3,0,0,0],3,[2,5,6],3))

