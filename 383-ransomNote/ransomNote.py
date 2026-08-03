def canConstruct(ransomNote, magazine):
    magazineChars = {}

    for char in magazine:
        if char not in magazineChars:
            magazineChars[char] = 1
        else:
            magazineChars[char] +=1

    for char in ransomNote:
        if char not in magazineChars or ransomNote.count(char) > magazineChars[char]:
            return False

    return True

ransomNote = "aa"
magazine = "ab"

print(canConstruct(ransomNote, magazine))