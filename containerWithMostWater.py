def maxArea(height):
    maxArea = 0
    low = 0
    high = len(height) - 1
    while low != high:
        if (min(height[low], height[high]) * (high - low)) > maxArea:
            maxArea = (min(height[low], height[high]) * (high - low))

        if height[low] <= height[high]:
            low +=1
        else:
            high -=1
    
    return maxArea

height = [1,8,6,2,5,4,8,3,7]

print(maxArea(height))