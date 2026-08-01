from collections import Counter


def intersect(nums1, nums2):
    if len(nums1) > len(nums2):
        return intersect(nums2, nums1)
    
    match = []
    count = Counter(nums1)

    for num in nums2:
        if count[num] > 0:
            match.append(num)
            count[num] -= 1
    
    return match

nums1 = [2,2]
nums2 = [1,2,2,1]

print(intersect(nums1, nums2))