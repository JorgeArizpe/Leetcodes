def intersection(nums1, nums2):
    match = set()
    nums = set(nums1)

    for num in nums2:
        if num in nums:
            match.add(num)
    
    return [num for num in match]

nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersection(nums1, nums2))