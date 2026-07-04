def threeSumClosest(nums, target):
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]

    for i in range(len(nums) - 2):
        high = len(nums) - 1
        low = i + 1

        while low < high:
            curr = nums[i] + nums[low] + nums[high]
            if abs(curr - target) < abs(closest - target):
                closest = curr

            if curr < target:
                low +=1
            elif curr > target:
                high -= 1
            else:
                return target

    return closest

nums = [0, 1, 2]
target = 0

print(threeSumClosest(nums,target))