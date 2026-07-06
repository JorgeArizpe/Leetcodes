# sus runtime pointer solution probs better
# might look into that later
def fourSum(nums, target):
    nums.sort()
    result = set()
    n = len(nums)

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                rest = target - nums[i] - nums[j] - nums[k]

                if rest in nums[k + 1 :]:
                    result.add((nums[i], nums[j], nums[k], rest))

    return [list(q) for q in result]


nums = [1, 0, -1, 0, -2, 2]
target = 0

print(fourSum(nums, target))
