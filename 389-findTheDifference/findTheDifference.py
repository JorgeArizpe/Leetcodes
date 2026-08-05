def findTheDifference(s, t):
    dictS = {}

    for char in s:
        if char not in dictS:
            dictS[char] = 1
        else:
            dictS[char] += 1
    
    for char in t:
        if char not in dictS or t.count(char) != dictS[char]:
            return char

s = "abcd"
t = "abcde"

print(findTheDifference(s, t))