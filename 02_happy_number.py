def isHappy(n):
    my_set = set()
    prev = n
    while prev not in my_set:
        my_set.add(prev)
        my_sum = 0
        for i in str(prev):
            my_sum += int(i) ** 2
        if my_sum == 1:
            return True
        prev = my_sum
    return False


print(isHappy(2))
print(isHappy(19))
