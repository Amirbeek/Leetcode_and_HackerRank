def findMaxHealthSum(health, serverType, m):
    type_to_health = {}
    for h, t in zip(health, serverType):
        if t in type_to_health:
            type_to_health[t] += h
        else:
            type_to_health[t] = h

    sums = list(type_to_health.values())
    sums.sort(reverse=True)
    max_health_sum = sum(sums[:m])
    return max_health_sum

health = [2, 3, 1, 4]
serverType = [1, 1, 2, 2]
m = 4
print(findMaxHealthSum(health, serverType, m))