def islandPerimeter(grid):
    if not grid:
        return 0

    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4
                if i != 0:
                    if grid[i - 1][j] == 1:
                        perimeter -= 2
                
                if j != 0:
                    if grid[i][j - 1] == 1:
                        perimeter -= 2
    
    return perimeter

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

print(islandPerimeter(grid))