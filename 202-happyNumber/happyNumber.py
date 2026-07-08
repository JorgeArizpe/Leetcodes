def isHappy(n):
    seen = []
    curr = n
    while True:
        if curr == 1:
            return True

        curr = sum(int(char)**2 for char in str(curr))

        if curr in seen:
            return False

        seen.append(curr)


n = 19
print(isHappy(n))
