def longestCommonPrefix(strs: list[str]) -> str:
    result = ""
    if len(strs) == 1:
        return strs[0]

    if min(strs):
        for i in range(len(min(strs))):
            next = strs[0][i]
            for s in strs:
                if s[i] != strs[0][i]:
                    return result
            result += next
    return result

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))