def isPalindrome(s: str):
    s = s.strip().lower()
    for char in s:
        if not (("a" <= char <= "z") or ("0" <= char <= "9")):
            s = s.replace(char, "")

    ln = len(s) - 1
    for i in range(ln):
        if s[i] != s[ln - i]:
            return False

    return True

s = "0P"

print(isPalindrome(s))
