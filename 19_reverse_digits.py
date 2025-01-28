def reverse_digits(num):
    result = 0
    number = abs(num)
    i = False if num < 0 else True
    while number > 0:
        result *= 10
        digit = number % 10
        number //=10
        result += digit

    return result if i else -result


def reverse_digits_2(num):
    result = 0
    number = abs(num)
    sign = -1 if num < 0 else 1

    while number > 0:
        result = result * 10 + number % 10
        number //= 10
        if result > 2147483647:
            return 0

    return result * sign


print(reverse_digits(1534236469))

print(reverse_digits(12345))
