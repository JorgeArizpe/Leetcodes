def toHex(num):
    if num == 0:
        return "0"

    if num < 0:
        num += 2**32

    hexa = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    result = []

    while num:
        result.append(hexa[num & 15])
        num //= 16

    return "".join(result[::-1])

num = 26

print(toHex(num))