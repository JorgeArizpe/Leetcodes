def isSubsequence(s, t):
    if s == t or not s:
        return True

    result = ""
    counter = 0

    for char in t:
        if char == s[counter]:
            result += char
            counter = min(counter + 1, len(s) - 1)
            
        if result == s:
            return True

    return False

s = ""
t = "ahbgdc"
print(isSubsequence(s, t))