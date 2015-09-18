# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

grid = (20, 20)
paths = [[0 for x in range(grid[0] + 1)] for x in range(grid[1] + 1)]

for x in range(grid[0], -1, -1):
    for y in range(grid[1], -1, -1):
        if grid[0] == x and grid[1] == y:
            paths[x][y] = 1
        elif grid[0] == x:
            paths[x][y] = paths[x][y + 1]
        elif grid[1] == y:
            paths[x][y] = paths[x + 1][y]
        else:
            paths[x][y] = paths[x + 1][y] + paths[x][y + 1]

print("Grid of size: {0}".format(grid))
print("{0} paths".format(paths[0][0]))