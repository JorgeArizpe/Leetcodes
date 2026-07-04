def isMatch(s, p):
    if not p:
        return not s

    charMatch = bool(s) and p[0] in {s[0], "."}

    if len(p) >= 2 and p[1] == "*":
        return isMatch(s, p[2:]) or charMatch and isMatch(s[1:], p)
    else:
        return charMatch and isMatch(s[1:], p[1:])

s = "ab"
p = ".*c"

print(isMatch(s, p))