def shiftGrid(grid, k):
    if not k:
        return grid

    col = len(grid[0])
    row = len(grid)
    n = col * row
    k %= n

    if not k:
        return grid

    def shift(i, j):
        while i < j:
            grid[i // col][i % col], grid[j // col][j % col] = grid[j // col][j % col], grid[i // col][i % col]
            i += 1
            j -= 1

    shift(0, n - 1)
    shift(0, k - 1)
    shift(k, n - 1)

    return grid

grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1

print(shiftGrid(grid, k))
