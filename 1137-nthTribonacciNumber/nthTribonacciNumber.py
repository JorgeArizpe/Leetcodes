def tribonacci(n):
    result = [0, 1, 1]

    while len(result) < n + 1:
        result.append(result[-1] + result[-2] + result[-3])
    
    return result[n]


n = 25

print(tribonacci(n))