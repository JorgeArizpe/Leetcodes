def findMaxConsecutiveOnes(nums):
    counter = 0
    maximum = 0
    for num in nums:
        if num == 1:
            counter += 1
        else:
            maximum = max(counter, maximum)
            counter = 0

    maximum = max(counter, maximum)

    return maximum

nums = [1,1,0,1,1,1]

print(findMaxConsecutiveOnes(nums))
