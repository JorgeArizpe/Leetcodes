def getRow(rowIndex):
    triangle = []

    for i in range(rowIndex + 1):
        curr = []

        curr.append(1)

        if i == 0:
            triangle.append(curr)
            continue

        while len(curr) < i:
            curr.append(triangle[i - 1][len(curr)] + triangle[i - 1][len(curr) - 1])

        curr.append(1)

        triangle.append(curr)

    return triangle[rowIndex]


rowIndex = 3

print(getRow(rowIndex))