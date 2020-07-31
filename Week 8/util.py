# Bandile Danxa
# Submission 2
# Date : 22 June 2020


# """create a 4x4 array of zeroes within grid"""
def create_grid(grid):
    grid.append([0,0,0,0])
    grid.append([0,0,0,0])
    grid.append([0,0,0,0])
    grid.append([0,0,0,0])

# """print out a 4x4 grid in 5-width columns within a box"""
def print_grid(grid):
    for row in range(len(grid)):
        for ele in grid[row]:
            print(str(ele).rjust(5), end =" ")
        print()
### Works fine

def noAdjacentEquals(grid):
    status = True
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(i < 3 and j < 3):
               if grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i][j+1]:  #compare element with the element below and one on the right
                   status = False
    if grid[1][3] == grid[0][3] or grid[1][3] == grid[2][3]:
        status = False
    if grid[3][3] == grid[3][2] or grid[3][3] == grid[2][3]:    #Check if adjacents of the last element in the grid are equal
        status = False
    return status
#### Works fine

# """Check lost, return True if there are no 0 values and there are no
# adjacent values that are equal; otherwise False"""
def check_lost(grid):
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] != 0 and noAdjacentEquals(grid):
                return True
    return False
### Seems to be working fine


# """return True if a value>=32 is found in the grid; otherwise False"""
def check_won(grid):
    for row in range(len(grid)):   # row range from 0 - 3
        for value in grid[row]:   # extract each element in the current row
            if value >= 32:     # check if the element is greater or equal to 32
                return True     # if that is the case then return True, meaning the user won
    return False
### Works fine


# """return a copy of the given grid"""
def copy_grid(grid):
    gridCopy = grid[:]
    return gridCopy
######## Looks fine

def grid_equal(grid1, grid2):
    grid1 = sorted(grid1)
    grid2 = sorted(grid2)
    if grid1 == grid2:
        return True
    return False
### Works fine

# grid1 = [[4,2,8,2],[2,8,16,8],[16,32,8,4],[4,8,4,2]]
# grid2 = [[4,2,8,2],[2,8,16,8],[16,32,8,4],[4,8,4,2]]
# print(grid_equal(grid1, grid2))