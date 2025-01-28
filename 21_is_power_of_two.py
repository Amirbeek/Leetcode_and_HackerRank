def isPowerOfTwo(n):
    if n <= 0: return False
    bit_count = 0
    while n != 0:
        digit = n & 1
        print(n)
        bit_count += digit
        n >>= 1

    return bit_count == 1
print(isPowerOfTwo(16))