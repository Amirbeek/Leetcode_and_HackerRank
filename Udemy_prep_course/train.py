def lonelyinteger(nums)->int:
    hash = {}
    for num in nums:
        if num not in hash:
            hash[num] = True
            continue
        del hash[num]
    return list(hash.keys())[0]


print(lonelyinteger([1, 2, 5, 2, 1]))
