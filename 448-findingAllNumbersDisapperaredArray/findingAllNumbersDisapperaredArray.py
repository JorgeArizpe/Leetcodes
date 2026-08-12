def findDisappearedNumbers(nums):
    n = len(nums)
    nums = set(nums)
    nums = [num for num in nums]
    nums.sort()
    result = []
    for i in range(n):
        if i + 1 not in nums:
            result.append(i + 1)
        else:
            nums.remove(i + 1)
    
    return result

nums = [4,3,2,7,8,2,3,1]

print(findDisappearedNumbers(nums))