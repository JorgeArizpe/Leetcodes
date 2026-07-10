# i did this one
def singleNumber(nums):
    seen = []

    for num in nums:
        if num not in seen:
            seen.append(num)
        else:
            seen.remove(num)
    
    return seen[0]

# XOR solution
def singleNumberXOR(nums):
    xor = 0
    for num in nums:
        xor ^= num
    
    return xor
    
nums = [4,1,2,1,2]

print(singleNumber(nums))