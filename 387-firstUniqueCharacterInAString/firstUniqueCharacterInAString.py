def firstUniqChar(s):
    seen = []
    for i in range(len(s)):
        if s[i] not in seen:
            if s.count(s[i]) == 1:
                return i
            seen.append(s[i])
    
    return -1

s = "leetcode"

print(firstUniqChar(s))