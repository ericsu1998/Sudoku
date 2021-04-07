
import copy

def hasDuplicates(L):
    return len(set(L)) != len(L)

def isSolved(board):
    #Checks if puzzle is unfinished 
    for row in board:
        if 0 in row: 
            return False

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

def getConstraints(board, row, col):
    res = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    res = res - set(board[row]) #Row constraints
    column = [board[r][col] for r in range(len(board))]
    res = res - set(column) #Column constraints
    rowStart = row // 3 * 3
    colStart = col // 3 * 3
    square = [board[r][c] for r in range(rowStart, rowStart + 3) for c in range(colStart, colStart + 3)]
    res = res - set(square) #Square constraints
    return list(res)

#Assumes there's at least one square in the board that is 0 (unfilled)
def getSquareWithMinimumConstraints(board):
    minConstraintsSquare = None 
    minConstraints = None 
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                constraints = getConstraints(board, r, c)
                if minConstraintsSquare == None or len(constraints) < len(minConstraints):
                    minConstraintsSquare = (r, c)
                    minConstraints = constraints

    return minConstraintsSquare, minConstraints 

def solve(board):
    if isSolved(board): return True, board
    (minConstraintSqR, minConstraintSqC), minConstraint = getSquareWithMinimumConstraints(board)
    for valueToTry in minConstraint:
        newBoard = copy.deepcopy(board)
        newBoard[minConstraintSqR][minConstraintSqC] = valueToTry
        solved, solution = solve(newBoard)
        if solved: return True, solution
    return False, []

if __name__ == "__main__":
    print("TODO: multi-sudoku extension")
        #first have gui?    
