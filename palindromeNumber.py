def isPalindrome(x: int) -> bool:
    left = 0
    newString = str(x)
    right = len(newString)-1

    while left < right:
        if newString[left] != newString[right]:
            return False
        left += 1
        right -=1
    return True


print(isPalindrome(0))