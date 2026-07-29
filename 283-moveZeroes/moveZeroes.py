def moveZeroes(nums):
    counter = 0

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == 0:
            counter += 1
            nums.pop(i)

    for _ in range(counter):
        nums.append(0)


nums = [0,1,0,3,12]

moveZeroes(nums)

print(nums)
