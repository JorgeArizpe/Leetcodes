def climbStairs(n):
    if n == 1:
        return 1

    oneBefore = 1
    twoBefore = 1
    totalSteps = 0

    for i in range(2, n + 1):
        totalSteps = oneBefore + twoBefore
        twoBefore = oneBefore
        oneBefore = totalSteps

    return totalSteps

print(climbStairs(1000))