def findPoisonedDuration(timeSeries, duration):
    result = 0
    n = len(timeSeries)
    for i in range(n):
        if i + 1 < n and timeSeries[i + 1] - timeSeries[i] < duration:
            result += timeSeries[i + 1] - timeSeries[i]
        else:
            result += duration 
        
    return result

timeSeries = [1,2,3,4,5]
duration = 5

print(findPoisonedDuration(timeSeries, duration))