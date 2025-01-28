def is_palidrome(string):
    low , high = 0, len(string) -1

    while low <= high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1
    return True

print(is_palidrome("aba"))
print('megafauna'[::-1])