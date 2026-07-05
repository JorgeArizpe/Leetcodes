def fib(n):
    result = [0,1]

    while len(result) < n + 1:
        result.append(result[-1] + result[-2])
    
    return result[n]

n = 30

print(fib(n))