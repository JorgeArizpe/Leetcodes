def myAtoi(s):
    result = ""
    negative = 1
    inNumbers = False
    sign = False
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    s = s.strip()
    for char in s:
        print(char)
        if char == "-" and not inNumbers and not sign:
            negative = -1
            sign = True
        elif char == "+" and not inNumbers and not sign:
            sign = True
        elif char in nums:
            result += char
            inNumbers = True
        else:
            break

    if len(result) < 1:
        return 0

    result = int(result)
    if result > ((2 ** 31) - 1) and negative > 0:
        result = ((2 ** 31) - 1)
    elif result > ((2 ** 31) - 1) and negative < 0:
        result = ((2 ** 31) - 1)
    return result * negative

s = "21474836460"
print(myAtoi(s))