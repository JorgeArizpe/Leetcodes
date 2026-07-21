def isPowerOfFour(n):
    if n == 1:
        return True

    if n % 4 != 0 or n < 1:
        return False

    return isPowerOfFour(n/4)

n = 16

print(isPowerOfFour(n))