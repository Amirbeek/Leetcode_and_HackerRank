def diagonalDifference(arr):
    dic = {}
    y = len(arr)-1
    for x, row in enumerate(arr):
         dic[(x,x)] = row[x]
         dic[(x,y)] = row[y]
         y-= 1
    return sum(dic.values())

arr =  [[1 ,2, 3],
        [4 ,5 ,6],
        [7, 8, 9]]
print(diagonalDifference(arr))