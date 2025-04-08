def covert_to_binary(num):
    result = ''
    while num != 0:
        digit = num % 2
        result += str(digit)
        num = num // 2
    return result[::-1]

print(covert_to_binary(12))



def convert_to_number(num):
    result = 0
    while num != 0:
        digit = num % 2
        result += digit
        num = num // 2
    print(result)

convert_to_number(1100)
