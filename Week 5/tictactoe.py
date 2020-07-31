# Name : Bandile Danxa
# Date : 03 June 2020
# Submission 1 - TicTacToe
# This is a tic tac toe program, lets two users play by taking turns


# Holds the data for our board game
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Lets us know if the game is still going or not
gameIsStillGoing = True

# Tells us who the winner is
winner = None

# Initialize the default value for player to be X and will hold the value for the current player
currentPlayer = "X"



# Play a game of tic tac toe
def playGame():

    # Show the initial game board
    displayBoard()

    # Loop until the game stops (winner or tie)
    while gameIsStillGoing:

        # Handle a turn
        handleTurn(currentPlayer)

        # Check if the game is over
        checkIfGameOver()

        # Flip to the other player
        flipPlayer()

    # Since the game is over, print who the winner or tie
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# Display the game board to the screen
def displayBoard():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2] + "\t\t\t 1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "\t\t\t 4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "\t\t\t 7 | 8 | 9\n")



# Handle player turns
def handleTurn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")        # Get position from player

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")    #prompt user to enter the position value

        # Convert position into an integer value and make sure the index is within our board list
        position = int(position) - 1

        # Check if the position is not already used
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Try again.")

    # Put the game piece on the board
    board[position] = player

    # Redisplay the game board
    displayBoard()


# Check if the game is over
def checkIfGameOver():
    checkForWinner()
    checkForTie()


# Check to see if somebody has won
def checkForWinner():
    global winner

    # Check if there was a winner anywhere
    rowWinner = checkRows()
    columnWinner = checkColumns()
    diagonalWinner = checkDiagonals()

    # Get the winner
    if rowWinner:
        winner = rowWinner
    elif columnWinner:
        winner = columnWinner
    elif diagonalWinner:
        winner = diagonalWinner
    else:
        winner = None


# Check the rows for a win
def checkRows():
    global gameIsStillGoing

    # Check if any of the rows have all the same value (and is not empty)
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    # If any row does have a match, flag that there is a win
    if row1 or row2 or row3:
        gameIsStillGoing = False

    # Return the winner
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
        # Or return None if there was no winner
    else:
        return None


# Check the columns for a win
def checkColumns():

    global gameIsStillGoing
    # Check if any of the columns have all the same value (and is not empty)
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if column1 or column2 or column3:
        gameIsStillGoing = False
    # Return the winner
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    else:
        return None


# Check the diagonals for a win
def checkDiagonals():
    global gameIsStillGoing

    # Check if any of the columns have all the same value (and is not empty)
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    # If any row does have a match, flag that there is a win
    if diagonal1 or diagonal2:
        gameIsStillGoing = False

    # Return the winner
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


# Check if there is a tie
def checkForTie():
    global gameIsStillGoing

    # If board is full
    if "-" not in board:
        gameIsStillGoing = False
        return True
    # else there is no tie
    else:
        return False


# Flip the current player from X to O, or O to X
def flipPlayer():
    global currentPlayer
    
    # If the current player was X, change it to O
    if currentPlayer == "X":
        currentPlayer = "O"        #update my cuurent player variable

    # if the current player was O, change it to X
    elif currentPlayer == "O":
        currentPlayer = "X"        #update my cuurent player variable



# Start playing the game
playGame()