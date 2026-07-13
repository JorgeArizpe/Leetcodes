def wordPattern(pattern, s: str):
    words = s.split()
    dictWords = {}
    dictPattern = {}
    n = len(pattern)

    if n != len(words):
        return False

    for i in range(n):
        if words[i] not in dictWords and pattern[i] not in dictPattern:
            dictWords[words[i]] = pattern[i]
            dictPattern[pattern[i]] = words[i]

        elif (words[i] in dictWords and dictWords[words[i]] != pattern[i]) or (pattern[i] in dictPattern and dictPattern[pattern[i]] != words[i]):
            return False

    return True

pattern = "abba"
s = "dog cat cat fish"

print(wordPattern(pattern, s))
