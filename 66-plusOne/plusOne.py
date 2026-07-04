def plusOne(digits):
    numbers = str(int("".join(str(digit) for digit in digits)) + 1)
    return list(int(number) for number in numbers)


digits = [1,2,3]
print(plusOne(digits))