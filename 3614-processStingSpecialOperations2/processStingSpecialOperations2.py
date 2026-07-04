def processStr(s, k):
    lens = []
    ln = 0

    for char in s:
        if char not in ["*", "#", "%"]:
            ln += 1
        elif char == "*":
            ln = max(ln - 1, 0)
        elif char == "#":
            ln += ln

        lens.append(ln)
        
    if k >= ln:
        return "."

    for i in range(len(s) - 1, -1, -1):
        c = s[i]
        if c == "*":
            continue
            
        elif c == "#":
            if k >= lens[i]//2:
                k -= lens[i]//2
                
        elif c == "%":
            k = lens[i] - 1 - k
            
        else:
            if lens[i] == k + 1:
                return c

s = "%#bz%xum##i##vzo#pwc*#dkwbh####%uf%s*%cgppqhqa%h#l##o%ij%%cz%iga##e###u%#e####jfwx##%%*x%m*%#"
k = 6523

print(processStr(s, k))