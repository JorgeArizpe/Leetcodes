def addBinary(a, b):
    result = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1

        if j >= 0:
            carry += int(b[j])
            j -= 1

        result.append(str(carry % 2))
        carry //= 2

    result.reverse()
    return "".join(result)

a = "1010"
b = "1011"

print(addBinary(a,b))