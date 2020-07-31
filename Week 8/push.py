# Bandile Danxa
# Submission 3
# Date : 23 June 2020

"""merge grid values upwards"""
def push_up(grid):
    row = 0
    count = 0
    for column in range(4):    # go from column 0 to 3
        while grid[row][column] == 0:
            if count < 4:
                # take element in row 1 and put it row 0
                grid[row][column] = grid[row+1][column]
                # take element in row 2 and put it row 1
                grid[row + 1][column] = grid[row+2][column]
                # take element in row 3 and put it row 2
                grid[row + 2][column] = grid[row+3][column]
                # reset value of element in row 3 of the current column
                grid[row + 3][column] = 0
            else:
                break
            count += 1
        count = 0
        while grid[row+1][column] == 0:
            if count < 3:
                # take element in row 2 and put it row 1
                grid[row + 1][column] = grid[row + 2][column]
                # take element in row 3 and put it row 2
                grid[row + 2][column] = grid[row + 3][column]
                # reset value of element in row 3 of the current column
                grid[row + 3][column] = 0
            else:
                break
            count += 1
        count = 0
        while grid[row + 2][column] == 0:
            if count < 2:
                # take element in row 3 and put it row 2
                grid[row + 2][column] = grid[row + 3][column]
                # reset value of element in row 3 of the current column
                grid[row + 3][column] = 0
            else:
                break
            count += 1

    for column in range(4): #go from column 0 to 3
        # is the element in row 0 equal to element in row 1?
        if grid[row][column] == grid[row+1][column]:
            # sum element in row 0 and element in row 1, store the result in row 0
            grid[row][column] += grid[row + 1][column]
            # update value of element in row 1
            grid[row + 1][column] = grid[row + 2][column]
            # update value of element in row 2
            grid[row + 2][column] = grid[row + 3][column]
            # reset value of element in row 3 of the current column
            grid[row + 3][column] = 0
            # is the element in row 1 equal to element in row 2?
            if grid[row+1][column] == grid[row+2][column]:
                # sum element in row 1 and element in row 2, store the result in row 1
                grid[row + 1][column] += grid[row + 2][column]
                # update value of element in row 2
                grid[row + 2][column] = grid[row + 3][column]

        # else is the element in row 1 equal to element in row 2?
        if grid[row+1][column] == grid[row+2][column]:
            # sum element in row 1 and element in row 2, store the result in row 1
            grid[row + 1][column] += grid[row + 2][column]
            # update value of element in row 2
            grid[row + 2][column] = grid[row + 3][column]
            # reset value of element in row 3 of the current column
            grid[row + 3][column] = 0
            # is the element in row 2 equal to element in row 3?
            if grid[row + 2][column] == grid[row + 3][column]:
                # sum element in row 2 and element in row 3, store the result in row 1
                grid[row + 2][column] += grid[row + 3][column]

        # else is the element in row 2 equal to element in row 3?
        if grid[row+2][column] == grid[row+3][column]:
            # sum element in row 2 and element in row 3, store the result in row 1
            grid[row + 2][column] += grid[row + 3][column]
            # reset value of element in row 3 of the current column
            grid[row + 3][column] = 0


"""merge grid values downwards"""
def push_down(grid):
    row = 0
    count = 0
    for column in range(4):  # go from column 0 to 3
        # as long as the element in row 3 and the current column is zero, loop 3 times
        while grid[row+3][column] == 0:
            if count < 4:
                # take element in row 2 and put it row 3
                grid[row + 3][column] = grid[row + 2][column]
                # take element in row 1 and put it row 2
                grid[row + 2][column] = grid[row + 1][column]
                # take element in row 0 and put it in row 1
                grid[row + 1][column] = grid[row][column]
                # reset value of element in row 0 of the current column
                grid[row][column] = 0
            else:
                break
            count += 1
        count = 0
        # as long as the element in row 2 and the current column is zero, loop 3 times
        while grid[row + 2][column] == 0:
            if count < 3:
                # take element in row 1 and put it row 2
                grid[row + 2][column] = grid[row + 1][column]
                # take element in row 0 and put it row 1
                grid[row + 1][column] = grid[row][column]
                # reset value of element in row 0 of the current column
                grid[row][column] = 0
            else:
                break
            count += 1
        count = 0
        while grid[row + 1][column] == 0:
            if count < 2:
                # take element in row 0 and put it row 1
                grid[row + 1][column] = grid[row][column]
                # reset value of element in row 0 of the current column
                grid[row][column] = 0
            else:
                break
            count += 1

    for column in range(4):  # go from column 0 to 3
        # is the element in row 3 equal to element in row 2?
        if grid[row+3][column] == grid[row + 2][column]:
            # sum element in row 3 and element in row 2, store the result in row 3
            grid[row+3][column] += grid[row + 2][column]
            # update value of element in row 2
            grid[row + 2][column] = grid[row + 1][column]
            # update value of element in row 1
            grid[row + 1][column] = grid[row][column]
            # reset value of element in row 0 of the current column
            grid[row][column] = 0
            # is the element in row 2 equal to element in row 1?
            if grid[row + 2][column] == grid[row + 1][column]:
                # sum element in row 2 and element in row 1, store the result in row 2
                grid[row + 2][column] += grid[row + 1][column]
                # update value of element in row 1
                grid[row + 1][column] = grid[row][column]
        # else is the element in row 2 equal to element in row 1?
        if grid[row + 2][column] == grid[row + 1][column]:
            # sum element in row 2 and element in row 1, store the result in row 2
            grid[row + 2][column] += grid[row + 1][column]
            # update value of element in row 1
            grid[row + 1][column] = grid[row][column]
            # reset value of element in row 0 of the current column
            grid[row][column] = 0
            # is the element in row 1 equal to element in row 0?
            if grid[row + 1][column] == grid[row][column]:
                # sum element in row 1 and element in row 0, store the result in row 1
                grid[row + 1][column] += grid[row][column]
        # else is the element in row 1 equal to element in row 3?
        if grid[row + 1][column] == grid[row][column]:
            # sum element in row 2 and element in row 3, store the result in row 1
            grid[row + 1][column] += grid[row][column]
            # reset value of element in row 3 of the current column
            grid[row][column] = 0


"""merge grid values left"""
def push_left(grid):
    column = 0
    count = 0
    for row in range(4):  # go from column 0 to 3
        while grid[row][column] == 0:
            if count < 4:
                # take element in column 1 and put it column 0
                grid[row][column] = grid[row][column + 1]
                # take element in column 2 and put it column 1
                grid[row][column + 1] = grid[row][column + 2]
                # take element in column 3 and put it column 2
                grid[row][column + 2] = grid[row][column + 3]
                # reset value of element in column 3 of the current column
                grid[row][column + 3] = 0
            else:
                break
            count += 1
        count = 0
        while grid[row][column + 1] == 0:
            if count < 3:
                # take element in column 2 and put it column 1
                grid[row][column + 1] = grid[row][column + 2]
                # take element in column 3 and put it column 2
                grid[row][column + 2] = grid[row][column + 3]
                # reset value of element in column 3 of the current column
                grid[row][column + 3] = 0
            else:
                break
            count += 1
        count = 0
        while grid[row][column + 2] == 0:
            if count < 2:
                # take element in column 3 and put it column 2
                grid[row][column + 2] = grid[row][column + 3]
                # reset value of element in column 3 of the current column
                grid[row][column + 3] = 0
            else:
                break
            count += 1

    for row in range(4):  # go from column 0 to 3
        # is the element in column 0 equal to element in row 1?
        if grid[row][column] == grid[row][column + 1]:
            # sum element in column 0 and element in column 1, store the result in column 0
            grid[row][column] += grid[row][column + 1]
            # Take element in column 2 and put it in column 1
            grid[row][column + 1] = grid[row][column + 2]
            # Take element in column 3 and put it in column 2
            grid[row][column + 2] = grid[row][column + 3]
            # reset value of element in column 3 of the current column
            grid[row][column + 3] = 0
            # is the element in row 1 equal to element in row 2?
            if grid[row][column + 1] == grid[row][column + 2]:
                # sum element in column 1 and element in column 2, store the result in column 1
                grid[row][column + 1] += grid[row][column + 2]
                # update value of element in column 2
                grid[row][column + 2] = grid[row][column + 3]

        # else is the element in column 1 equal to element in column 2?
        if grid[row][column + 1] == grid[row][column + 2]:
            # sum element in column 1 and element in column 2, store the result in column 1
            grid[row][column + 1] += grid[row][column + 2]
            # update value of element in column 2
            grid[row][column + 2] = grid[row][column + 3]
            # reset value of element in column 3 of the current column
            grid[row][column + 3] = 0
            # is the element in column 2 equal to element in column 3?
            if  grid[row][column + 2] == grid[row][column + 3]:
                # sum element in column 2 and element in column 3, store the result in column 2
                grid[row][column + 2] = grid[row][column + 3]

        # else is the element in row 2 equal to element in row 3?
        if grid[row][column + 2] == grid[row][column + 3]:
            # sum element in column 2 and element in column 3, store the result in column 2
            grid[row][column + 2] = grid[row][column + 3]
            # reset value of element in column 3 of the current column
            grid[row][column + 3] = 0


"""merge grid values right"""
def push_right(grid):
    column = 0
    count = 0
    for row in range(4):  # go from column 0 to 3
        while grid[row][column + 3] == 0:
            if count < 4:
                # take element in column 2 and put it column 3
                grid[row][column + 3] = grid[row][column + 2]
                # take element in column 1 and put it column 2
                grid[row][column + 2] = grid[row][column + 1]
                # take element in column 0 and put it column 1
                grid[row][column + 1] = grid[row][column]
                # reset value of element in column 0 of the current row
                grid[row][column] = 0
            else:
                break
            count += 1
        count = 0
        while grid[row][column + 2] == 0:
            if count < 3:
                # take element in column 1 and put it column 2
                grid[row][column + 2] = grid[row][column + 1]
                # take element in column 0 and put it column 1
                grid[row][column + 1] = grid[row][column]
                # reset value of element in column 0 of the current row
                grid[row][column] = 0
            else:
                break
            count += 1
        count = 0
        while grid[row][column + 1] == 0:
            if count < 2:
                # take element in column 0 and put it column 1
                grid[row][column + 1] = grid[row][column]
                # reset value of element in column 0 of the current row
                grid[row][column] = 0
            else:
                break
            count += 1

    for row in range(4):  # go from row 0 to 3
        # is the element in column 3 equal to element in column 2?
        if grid[row][column + 3] == grid[row][column + 2]:
            # sum element in column 3 and element in column 2, store the result in column 3
            grid[row][column + 3] += grid[row][column + 2]
            # update value of element in column 2
            grid[row][column + 2] = grid[row][column + 1]
            # update value of element in column 1
            grid[row][column + 1] = grid[row][column]
            # reset value of element in row 0 of the current column
            grid[row][column] = 0
            # is the element in column 2 equal to element in column 1?
            if grid[row][column + 2] == grid[row][column + 1]:
                # sum element in column 2 and element in column 1, store the result in column 2
                grid[row][column + 2] += grid[row][column + 1]
                # update value of element in column 1
                grid[row][column + 1] = grid[row][column]

        # else is the element in column 2 equal to element in column 1?
        if grid[row][column + 2] == grid[row][column + 1]:
            # sum element in column 2 and element in column 1, store the result in row 2
            grid[row][column + 2] += grid[row][column + 1]
            # update value of element in column 1
            grid[row][column + 1] = grid[row][column]
            # reset value of element in row 0 of the current column
            grid[row][column] = 0
            # is the element in column 1 equal to element in column 0?
            if grid[row][column + 1] == grid[row][column]:
                # sum element in column 1 and element in column 0, store the result in column 1
                grid[row][column + 1] += grid[row][column]

        # else is the element in column 1 equal to element in column 3?
        if grid[row][column + 1] == grid[row][column]:
            # sum element in column 1 and element in column 0, store the result in column 1
            grid[row][column + 1] += grid[row][column]
            # reset value of element in row 3 of the current column
            grid[row][column] = 0
