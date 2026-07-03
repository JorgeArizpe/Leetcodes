def threeSum(nums):
    nums.sort()
    res = set()
    n = len(nums)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            x = -(nums[i] + nums[j])

            if x in nums[j + 1:]:
                res.add((nums[i], nums[j], x))

    return [list(t) for t in res]

def threeSumGood(nums):
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, n - 1

        while l < r:
            s = nums[i] + nums[l] + nums[r]

            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1

                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1

            elif s < 0:
                l += 1
            else:
                r -= 1

    return res

nums = [-1,0,1,2,-1,-4]

print(threeSumGood(nums))