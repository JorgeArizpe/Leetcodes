def isValid(s):
    stack = [""]
    openings = ["(", "[", "{"]
    corrects = {")": "(", "}": "{", "]": "["}
    for symbol in s:
        if symbol in openings:
            stack.append(symbol)
        elif stack[-1] == corrects[symbol]:
            stack.pop()
        elif stack[-1] != corrects[symbol]:
            return False
    print(len(stack))
    if len(stack) == 1:
        return True
    return False


s = ")"
print(isValid(s))