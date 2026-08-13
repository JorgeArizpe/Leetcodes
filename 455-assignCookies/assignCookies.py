def findContentChildren(g, s):
    result = 0

    if not g or not s or min(g) > max(s):
        return result

    g.sort()
    s.sort()

    for i in g:
        for j in s:
            if i <= j:
                print(i,j)
                result += 1
                s.remove(j)
                break

    return result

g = [1,2,3]
s = [1,1]
print(findContentChildren(g, s))
