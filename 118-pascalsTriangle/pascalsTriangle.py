def generate(numRows):
    triangle = []

    for i in range(numRows):
        curr = []

        curr.append(1)

        if i == 0:
            triangle.append(curr)
            continue

        if i == 1:
            curr.append(1)
            triangle.append(curr)
            continue

        while len(curr) < i:
            curr.append(triangle[i - 1][len(curr)] + triangle[i - 1][len(curr) - 1])

        curr.append(1)

        triangle.append(curr)

    return triangle


numRows = 5

print(generate(numRows))
