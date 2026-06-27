def removeDuplicates(nums):
    dupeIdx = []
    for element in range(len(nums)-1):
        curr = nums[element]
        if nums[element+1] == curr:
            dupeIdx.append(element+1)

    dupeIdx.sort(reverse=True)
    for dupe in dupeIdx:
        nums.pop(dupe)

    return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
expectedNums = [0,1,2,3,4]

k = removeDuplicates(nums)

assert k == len(expectedNums)

for num in range(len(expectedNums)):
    assert nums[num] == expectedNums[num]

print(nums)
print(expectedNums)