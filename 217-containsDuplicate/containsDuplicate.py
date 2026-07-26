from collections import defaultdict


def containsDuplicate(nums):
    dict = defaultdict(int)

    for num in nums:
        if dict[num]:
            return True

        dict[num] = True

    return False

nums = [1,2,3,1]

print(containsDuplicate(nums))
