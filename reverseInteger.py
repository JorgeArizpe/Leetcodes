def reverse(x):
    negative = False
    numbersStringList = list(str(x))

    if numbersStringList[0] == "-":
        numbersStringList.pop(0)
        negative = True

    numbersStringList.reverse()
    newX = int("".join(numbersStringList))

    if abs(newX) > (2 ** 31) - 1:
        return 0

    if negative:
        newX *= -1

    return newX

x = 1563847412
print(reverse(x))