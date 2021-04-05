
def hasDuplicates(L):
    return len(set(L)) != len(L)

def verifySolution(board):
    #Checks row duplicates
    for row in board:
        if hasDuplicates(row):
            return False

    #Check column duplicates
    for col in range(len(board[0])):
        column = [board[row][col] for row in range(len(board))]
        if hasDuplicates(column): 
            return False
    
    #Check square duplicates
    for rowSquare in range(3):
        for colSquare in range(3):
            square = [board[row][col] for row in range(rowSquare * 3, (rowSquare + 1) * 3)
                                      for col in range(colSquare * 3, (colSquare + 1) * 3)]
            if hasDuplicates(square):
                return False
    return True

if __name__ == "__main__":
    print("TODO: sudoku solver")