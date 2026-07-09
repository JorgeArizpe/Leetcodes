from collections import defaultdict


def findDuplicate(nums):
    seen = defaultdict(int)

    for num in nums:
        if seen[num] > 0:
            return num
        seen[num] += 1

    return -1

nums = [1,3,4,2,2]

print(findDuplicate(nums))
