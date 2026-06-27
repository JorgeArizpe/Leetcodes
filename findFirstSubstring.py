def strStr(haystack, needle):
    if len(needle) > len(haystack):
        return -1
    
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i] == needle[0]:
            count = 0
            for j in range(len(needle)):
                if needle[j] != haystack[i+j]:
                    break
                count += 1
            if count == len(needle):
                return i
    return -1



haystack = "mississippi"
needle = "issipi"
index = -1

result = strStr(haystack,needle)

assert result == index