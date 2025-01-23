def miniMaxSum(arr):
    min,max = 0,0
    sorted_arr = sorted(arr)
    for index, num in enumerate(sorted_arr):
        if index >= 0 and index < len(arr)-1:
            min += num
        if index > 0:
            max += num
    print(min,max)
miniMaxSum([7, 69, 2, 221, 8974])