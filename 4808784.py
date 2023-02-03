# this isn't like an attempt to solve the problem, i just want to save this snippet on dmoj itself so i dont lose it
while 1:1

def fuse(grid):
    delta = False
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1] and grid[i][j] != 0:
                grid[i][j] = mat[i][j] * 2
                grid[i][j+1] = 0
                delta = True
    return grid,delta