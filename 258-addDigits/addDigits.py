def addDigits(num):
    if num == 0:
        return 0
    return 1 + (num - 1) % 9 # Formula for digital root

num = 0
print(addDigits(num))
