def generateParenthesis(n):
    result = []

    def make(open, close, s):
        if len(s) == n * 2:  # number of parenthese * amount of characters per
            result.append(s)
            return

        if open < n:  # number of "(" less than amount of parentheses allowed
            make(open + 1, close, s + "(")
        if close < open:  # number of ")" less than number of "("
            make(open, close + 1, s + ")")

    make(0, 0, "")
    return result


n = 3

print(generateParenthesis(n))
