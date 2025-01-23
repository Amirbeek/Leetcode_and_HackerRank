def findScore(userID1, userID2, p):
    from collections import Counter
    userID2_count = Counter(userID2)
    m = len(userID2)
    max_length = (m - 1) * p + 1
    score = 0

    for start in range(min(p, len(userID1))):
        current_count = Counter()

        for j in range(start, start + max_length, p):
            if j >= len(userID1):
                break
            current_count[userID1[j]] += 1

        if current_count == userID2_count:
            score += 1

        for j in range(start + p, len(userID1), p):
            if j + (m - 1) * p >= len(userID1):
                break

            exit_char = userID1[j - p]
            current_count[exit_char] -= 1
            if current_count[exit_char] == 0:
                del current_count[exit_char]

            new_char = userID1[j + (m - 1) * p]
            current_count[new_char] += 1

            if current_count == userID2_count:
                score += 1

    return score


# Example test
userID1 = "zxyzxxyz"
userID2 = "xxzy"
p = 1
print(findScore(userID1, userID2, p))  # Output should be 2
