def romanToInt(s: str) -> int:
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    length = len(s) - 1
    counter = 0
    
    while counter < length + 1:
        left = romans[s[length - counter]]
        right = romans[s[length - counter - 1]]
        result += left
        if left > right and length - counter !=0:
            result -= right
            counter += 2
        else:
            counter += 1

print(romanToInt("MMMCDXC"))