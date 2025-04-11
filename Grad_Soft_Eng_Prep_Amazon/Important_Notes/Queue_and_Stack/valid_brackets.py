def valid_brackets(s: str) -> bool:
    stack = []
    brackets = {
        "}": "{",
        ")": "(",
        "]": "["
    }

    for char in s:
        if char not in brackets:
            stack.append(char)
            continue

        if not stack:
            return False

        last_opened = stack.pop()
        if last_opened != brackets[char]: #'{ ' if not equle of value of "{" , bc when we are calling barckets[char] this return value
            return False

    return not len(stack)

test_cases = [
    ("()", True),
    # ("([])", True),
    # ("({[]})", True),
    # ("(]", False),
    # ("([)]", False),
    # ("{[}", False),
    # ("", True),
    # ("(((", False),
    # ("(()())", True)
]

for s, expected in test_cases:
    result = valid_brackets(s)
    # print(f"Input: {s:8} → Output: {result} | Expected: {expected} | {'✅' if result == expected else '❌'}")

