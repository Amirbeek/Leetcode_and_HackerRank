def Reverse_String(s: str) -> str:
    if not s or len(s) < 2:
        return s
    basket = []

    for char in s:
        basket.append(char)
        print(basket)
    result = ''.join(basket[::-1])
    return result


def reverse_two(s: str)->str:
    return s[::-1]

# Testing the function
print(reverse_two('Amir'))
