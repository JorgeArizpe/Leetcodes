def longestPalindrome(s):
    def isPalindrome(s):
        left = 0
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -=1
        return True
    
    longest = ""
    if isPalindrome(s):
        return(s)
    
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if isPalindrome(s[i:j]) and len(s[i:j]) > len(longest):
                longest = s[i:j]
    return longest

s = "babad"
print(longestPalindrome(s))