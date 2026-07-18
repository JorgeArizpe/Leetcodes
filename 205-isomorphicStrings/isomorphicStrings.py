def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    def build(s):
        dict = {}
        newString = ""
        counter = 0
        for char in s:
            if char not in dict:
                dict[char] = counter
                counter += 1

        for char in s:
            newString += str(dict[char]) + " "

        return newString

    return build(s) == build(t)


s = "abcdefghijklmnopqrstuvwxyzva"
t = "abcdefghijklmnopqrstuvwxyzck"

print(isIsomorphic(s, t))
