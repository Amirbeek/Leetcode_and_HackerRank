def plusMinus(arr):
    pos, neg, zero = 0, 0, 0
    arr_len = len(arr)
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1

    print(pos / arr_len)
    print(neg / arr_len)
    print(zero / arr_len)

# Example usage:
plusMinus([1, -1, 0, 1, -1])
