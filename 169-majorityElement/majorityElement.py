def majorityElement(nums):
    seen = []
    for num in nums:
        if num in seen:
            continue
        
        if nums.count(num) > len(nums) / 2:
            return num

        seen.append(num)

nums = [2,2,1,1,1,2,2]

print(majorityElement(nums))