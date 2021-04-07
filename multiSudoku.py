
import copy
import time 

def printBoard(board):
    for r in range(3):
        print("|", end = "")
        for c in range(9):
            val = board[(r, c)]
            printVal = "_" if val == None else val
            if c == 8:
                print(printVal, end = "")
            else: 
                print("{}|".format(printVal), end = "")
        print("|")

    for r in range(3, 9):
        print("|", end = "")
        for c in range(12):
            val = board[(r, c)]
            printVal = "_" if val == None else val
            if c == 11:
                print(printVal, end = "")
            else: 
                print("{}|".format(printVal), end = "")
        print("|")
    
    for r in range(9, 12):
        print("      |", end = "")
        for c in range(3, 12):
            val = board[(r, c)]
            printVal = "_" if val == None else val
            if c == 11:
                print(printVal, end = "")
            else: 
                print("{}|".format(printVal), end = "")
        print("|")                
    
#squares: list of (r, c, value) pairs
def makeBoard(squares):
    board = {}
    for r in range(12):
        for c in range(12):
            if (r < 3 and c > 8) or (r > 8 and c < 3): continue
            board[(r, c)] = None 
    for r, c, v in squares:
        board[(r, c)] = v
    return board

def hasDuplicates(L):
    return len(set(L)) != len(L)

#Does this actually need to be done? Prob
def isSolved(board):
    # Is puzzle unsolved
    if None in board.values(): return False
    # Checks row duplicates

    # Checks column duplicates

    # Checks square duplicates
    for rowSquare in range(4):
        for colSquare in range(4):
            if (not(rowSquare == 4 and colSquare == 1 or rowSquare == 1 and colSquare == 4)):
                square = [board[(r, c)] for r, c in board.keys() if r // 3 == rowSquare and c // 3 == colSquare]
                if hasDuplicates(square): 
                    return False 

    return True 

def getConstraints(board, row, col):
    res = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for position, v in board.items():
        r, c = position 
        if ((r == row and abs(c // 3 - col // 3) <= 2)
            or (c == col and abs(r // 3 - row // 3) <= 2)
            or (r // 3 == row // 3 and c // 3 == col // 3)):
            res.discard(v)
    return res

def getSquareWithMinimumConstraints(board):
    minConstraintsSquare = None 
    minConstraints = None 
    for position, v in board.items():
        r, c = position
        if v == None:
            constraints = getConstraints(board, r, c)
            if (minConstraints == None or len(constraints) < len(minConstraints)):
                minConstraintsSquare = (r, c)
                minConstraints = constraints
    return minConstraintsSquare, minConstraints

def solve(board):
    if isSolved(board): return True, board 
    minConstraintPos, minConstraint = getSquareWithMinimumConstraints(board)
    if minConstraintPos == None: return False, None
    r, c = minConstraintPos
    for valueToTry in minConstraint:
        newBoard = copy.deepcopy(board)
        newBoard[(r, c)] = valueToTry
        solved, solution = solve(newBoard)
        if solved: return True, solution
    return False, None   

if __name__ == "__main__":
    board = makeBoard([(0, 0, 5), (0, 4, 7), (0, 7, 8), (0, 8, 2),
                       (1, 3, 9), (1, 4, 1), (2, 6, 9), (2, 7, 3),
                       (4, 0, 6), (4, 1, 7), (4, 6, 4), (4, 9, 3), (4, 11, 6),
                       (3, 1, 5), (3, 6, 8), (3, 11, 5), (5, 7, 9), (5, 8, 3), 
                       (5, 9, 8), (6, 2, 4), (6, 3, 3), (6, 4, 5),
                       (7, 0, 9), (7, 2, 6), (7, 5, 2), (7, 10, 6), (7, 11, 8),
                       (8, 0, 1), (8, 5, 6), (8, 10, 5), (9, 4, 1), (9, 5, 8), 
                       (10, 7, 7), (10, 8, 1), (11, 3, 4), (11, 4, 7),
                       (11, 7, 8), (11, 11, 1)])
    printBoard(board)
    solved, solution = solve(board)
    print(solved)
    printBoard(solution)
