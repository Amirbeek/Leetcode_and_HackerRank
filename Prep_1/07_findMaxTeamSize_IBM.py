from collections import Counter
def findMaxTeamSize(skills):
    if not skills:
        return 0

    count = Counter(skills)
    sortedSkills = sorted(count.keys())

    maxSize = 0
    current = count[sortedSkills[0]]

    for i in range(1, len(sortedSkills)):
        if sortedSkills[i] == sortedSkills[i - 1] + 1:
            current += count[sortedSkills[i]]
        else:
            maxSize = max(maxSize, current)
            current = count[sortedSkills[i]]

    maxSize = max(maxSize, current)
    return maxSize

print(findMaxTeamSize([10,12,13,9,14]))