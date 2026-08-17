def licenseKeyFormatting(s, k):
    result = ""
    curr = ""
    for i in range(len(s) - 1, -1, -1):
        if s[i] != "-":
            curr = s[i].upper() + curr

        if len(curr) >= k:
            result = curr + "-" + result
            curr = ""

    if curr:
        result = curr + "-" + result
        
    return result[:-1]

s = "5F3Z-2e-9-w"
k = 4

print(licenseKeyFormatting(s, k))