def arrangeCoins(n):
    if n == 1:
        return 1
    curr = 0
    for i in range(1, n + 1):
        if curr + i > n:
            return i - 1
        curr += i

n = 8

print(arrangeCoins(n))