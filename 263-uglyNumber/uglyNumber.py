def isUgly(n):
    for i in 2, 3, 5:
        while n % i == 0 < n:
            n /= i

    return n == 1

n = 14

print(isUgly(n))
