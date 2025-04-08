def lonelyinteger(a):
    hashed = {}
    for x in a:
        if x in hashed:
            hashed[x] = False
        else:
            hashed[x] = True
    ans = [key for key, value in hashed.items() if value]
    return ans[0]

print(lonelyinteger([1,1,2,2,4,3,3]))