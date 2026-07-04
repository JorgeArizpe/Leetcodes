def threeSumClosest(nums, target):
    closest = sum(nums[0:2])

    for i in range(len(nums) - 2):
        if (target - sum(nums[i:i + 3])) < closest:
            closest = sum(nums[i:i + 3])

    return closest

nums = [-1,2,1,-4]
target = 1

print(threeSumClosest(nums,target))