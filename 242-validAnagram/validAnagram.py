def isAnagram(s, t):
    if len(s) != len(t):
        return False

    dictS = {}
    dictT = {}

    for char in s:
        if char not in dictS:
            dictS[char] = 1
        else: 
            dictS[char] += 1

    for char in t:
        if char not in dictT:
            dictT[char] = 1
        else: 
            dictT[char] += 1

    return dictS == dictT

s = "rat"
t = "cat"

print(isAnagram(s, t))