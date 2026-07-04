def mySqrt(x):
    low = 0
    high = x

    while low <= high:
        middle = (low + high)//2
        print(middle)
        if middle * middle == x:
            return middle

        if middle * middle < x:
            low = middle + 1

        else:
            high = middle - 1

    return high

print(mySqrt(8))