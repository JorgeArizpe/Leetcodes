def sequentialDigits(low, high):
    numbers = [*range(1,10)]

    for number in numbers:
        x = number % 10
        if x < 9:
            numbers.append(number * 10 + x + 1)

    return [number for number in numbers if low <= number <= high]

low = 10
high = 1000000000

print(sequentialDigits(low, high))
