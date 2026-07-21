def isPowerOfThree(n):
    if n == 1:
        return True

    if n % 3 != 0 or n < 1:
        return False

    return isPowerOfThree(n/3)

n = 27

print(isPowerOfThree(n))