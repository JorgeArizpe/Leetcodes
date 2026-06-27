def lengthOfLastWord(s):
    words = s.split(" ")
    for i in range(words.count("")):
        words.remove("")

    return len(words[-1])


s = "   fly me   to   the moon  "

print(lengthOfLastWord(s))