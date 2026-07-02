def intToRoman(num):
    result = ""
    
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    for i in range(len(symbols)):
        while num >= values[i]:
            num -= values[i]
            result += symbols[i]

    return result     

num = 3749

print(intToRoman(num))