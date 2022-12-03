from model.island import *
# import sys
# sys.setrecursionlimit(3500)

def islandCount(grid):
    visited = set()
    count = 0
    for row in range(0, len(grid)):
        for col in range(0,len(grid[0])):
            if explore(grid,row,col,visited) == True:
                count += 1

    return count            


def explore(grid,row,col,visited):
    rowInBounds = 0<=row and row < len(grid)
    colInBounds = 0<=col and col < len(grid[0])
    if (not rowInBounds ) or (not colInBounds ): return False
    
   
    if grid[row][col] == 'W': return False

    pos = str(row) + "," + str(col)

    if pos in visited: return False

    visited.add(pos)

    explore(grid,row+1,col,visited)
    explore(grid,row-1,col,visited)
    explore(grid,row,col+1,visited)
    explore(grid,row,col-1,visited)

    return True


print(islandCount(islandGrid))