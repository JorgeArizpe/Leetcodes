def processStr(s):
    result = []

    for char in s:
        if char not in ["*", "#", "%"]:
            result.append(char)
        elif char == "*":
            if len(result) > 0:
                result.pop()
        elif char == "#":
            result.extend(result)
        elif char == "%":
            result.reverse()

    return "".join(result)

s = "a#b%*"

print(processStr(s))