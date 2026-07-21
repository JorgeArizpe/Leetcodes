def isPowerOfTwo(n):
    if n == 1:
        return True

    if n % 2 != 0 or n < 1:
        return False

    return isPowerOfTwo(n/2)

n = 5

print(isPowerOfTwo(n))