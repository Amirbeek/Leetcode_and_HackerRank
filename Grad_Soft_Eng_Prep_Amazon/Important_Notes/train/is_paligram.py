def testing(s: str) -> bool:
    arr = []
    baskets = {
        "}": "{",
        ")": "(",
        "]": "["
    }
    for char in s:
        if char not in baskets:
            arr.append(char)
            continue

        if not arr:
            return False

        last_append = arr.pop()
        if last_append != baskets[char]:
            return False

        return not len(arr)


print(testing('()'))



