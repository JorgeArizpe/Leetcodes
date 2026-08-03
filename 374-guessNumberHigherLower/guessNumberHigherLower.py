def guessNumber(n):
    left = 1
    right = n

    while left < right:
        mid = (left + right)//2
        curr = guess(mid)

        if curr == 0:
            return mid

        elif curr == 1:
            left = mid + 1

        else:
            right = mid - 1

    return left
