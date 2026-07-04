def removeElement(nums, value):
    toRemove = nums.count(value)

    for i in range(toRemove):
        nums.remove(value)

    return len(nums)


nums = [0,1,2,2,3,0,4,2]
expectedNums = [0,1,4,0,3]
val = 2

k = removeElement(nums, val)

print(nums)
print(expectedNums)

assert k == len(expectedNums)

for num in range(len(expectedNums)):
    assert nums[num] in(expectedNums)