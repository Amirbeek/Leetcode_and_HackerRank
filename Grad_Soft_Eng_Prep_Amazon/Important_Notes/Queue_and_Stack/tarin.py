def val_basket(s: str) -> bool:
    arr = [] # (
    my_bas = {
        "]": "[",
        "}": "}",
        ")": "("
    }

    for char in s:
        if char not in my_bas: # )
            arr.append(char)

        if not arr:
            return False

        last_value = arr.pop()

        if last_value != my_bas[char]:
            return False

        return not len(arr)
