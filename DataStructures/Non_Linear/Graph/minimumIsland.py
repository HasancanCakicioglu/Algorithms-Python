from model.island import *

def minimumIsland(grid):
    visited = set()

    minSize = float('inf')
    for row in range(0, len(grid)):
        for col in range(0,len(grid[0])):
            size = exploreSize(grid,row,col,visited)
            if size > 0 and size < minSize:
                minSize = size

    return minSize


def exploreSize(grid,row,col,visited):
    rowInBounds = 0<=row and row < len(grid)
    colInBounds = 0<=col and col < len(grid[0])
    if (not rowInBounds ) or (not colInBounds ): return 0
    
   
    if grid[row][col] == 'W': return 0

    pos = str(row) + "," + str(col)

    if pos in visited: return 0

    visited.add(pos)


    size = 1
    size += exploreSize(grid,row+1,col,visited)
    size += exploreSize(grid,row-1,col,visited)
    size += exploreSize(grid,row,col+1,visited)
    size += exploreSize(grid,row,col-1,visited)
    return size

    return True


print(minimumIsland(islandGrid))