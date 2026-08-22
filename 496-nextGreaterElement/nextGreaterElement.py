def nextGreaterElement(nums1, nums2):
    result = []
    for i in range(len(nums1)):
        n = nums2.index(nums1[i])
        added = False
        for j in range(n + 1, len(nums2)):
            if nums2[j] > nums1[i]:
                result.append(nums2[j])
                added = True
                break
        if not added:
            result.append(-1)

    return result

nums1 = [4,1,2]
nums2 = [1,3,4,2]

print(nextGreaterElement(nums1, nums2))