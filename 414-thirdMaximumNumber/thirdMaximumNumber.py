def thirdMax(nums):
    nums = set(nums)
    nums = [num for num in nums]
    nums.sort()
    if len(nums) < 3:
        return max(nums)
    return nums[-3]

nums = [2,2,3,1]

print(thirdMax(nums))