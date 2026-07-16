def gdcsum(nums):
    def findGCD(a, b):
        if a == 0:
            return b
        return findGCD(b % a, a)

    gcdList = []
    result = 0
    max = 0

    for i in range(len(nums)):
        if  nums[i] > max:
            max =  nums[i]
        gcdList.append(findGCD(max, nums[i]))

    gcdList.sort()
    n = len(gcdList) - 1

    for i in range((n+ 1)//2):
        result += findGCD(gcdList[i], gcdList[n - i])
    
    return result

nums = [2,6,4]
nums2 = [3,6,2,8]

print(gdcsum(nums))
print(gdcsum(nums2))