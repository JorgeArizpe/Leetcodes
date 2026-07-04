def letterCombinations(digits):
    list = []
    if not digits:
        return list
    
    numberValues = {
        "2": ["a", "b", "c"], 
        "3": ["d", "e", "f"], 
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m","n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    def makeList(index, curr):
        if index == len(digits):
            list.append(curr)
            return

        for letter in numberValues[digits[index]]:
            makeList(index + 1, curr + letter)
        

    makeList(0, "")
    return list

digits = "23"

print(letterCombinations(digits))