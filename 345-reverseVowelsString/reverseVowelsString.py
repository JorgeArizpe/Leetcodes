def reveseVowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    indexes = []
    chars = []
    s = list(s)

    for i in range(len(s)):
        if s[i].lower() in vowels:
            indexes.append(i)
            chars.append(s[i])

    n = len(indexes)
    print(indexes, chars)

    for i in range(n):
        s[indexes[i]] = chars[n - i - 1]
    
    return "".join(s)

s = "IceCreAm"

print(reveseVowels(s))