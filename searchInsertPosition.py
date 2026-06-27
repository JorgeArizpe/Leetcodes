def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right)//2

        if target == nums[middle]:
            return middle

        if target > nums[middle]:
            left = middle + 1

        else:
            right = middle - 1

    return left


nums = [1,3,5,6]
target = 2

print(searchInsert(nums, target))