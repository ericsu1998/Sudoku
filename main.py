
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

# Testing Methods
def testHasDuplicates(): 
    print("Testing hasDuplicates()...")
    print("Testing no duplicates")
    noDuplicates = [1, 2, 3]
    assert(not hasDuplicates(noDuplicates))
    print("Testing duplicates")
    duplicates = [1, 2, 1]
    assert(hasDuplicates(duplicates))
    print("")

def testVerifySolution():
    #last row has two 0's
    print("Testing verifySolution()...")
    print("Testing row duplicates")
    testRowDuplicates = [
        [1, 8, 2, 6, 3, 4, 9, 7, 5],
        [4, 7, 9, 2, 8, 5, 3, 1, 6],
        [3, 6, 5, 9, 7, 1, 2, 4, 8],
        [5, 4, 7, 1, 9, 3, 6, 8, 2],
        [9, 3, 6, 7, 2, 8, 1, 5, 4],
        [2, 1, 8, 5, 4, 6, 7, 3, 9],
        [8, 2, 3, 4, 1, 9, 5, 6, 7],
        [6, 9, 4, 3, 5, 7, 8, 2, 1],
        [0, 5, 1, 8, 6, 2, 4, 9, 0]
    ]
    print("Testing col duplicates")
    assert(not verifySolution(testRowDuplicates))
    #last column has two 0's
    testColDuplicates = [
        [1, 8, 2, 6, 3, 4, 9, 7, 0],
        [4, 7, 9, 2, 8, 5, 3, 1, 6],
        [3, 6, 5, 9, 7, 1, 2, 4, 8],
        [5, 4, 7, 1, 9, 3, 6, 8, 2],
        [9, 3, 6, 7, 2, 8, 1, 5, 4],
        [2, 1, 8, 5, 4, 6, 7, 3, 9],
        [8, 2, 3, 4, 1, 9, 5, 6, 7],
        [6, 9, 4, 3, 5, 7, 8, 2, 1],
        [7, 5, 1, 8, 6, 2, 4, 9, 0]
    ]
    assert(not verifySolution(testColDuplicates))
    print("Testing square duplicates")
    #bottom right square has two 0's
    testSquareDuplicates = [
        [1, 8, 2, 6, 3, 4, 9, 7, 5],
        [4, 7, 9, 2, 8, 5, 3, 1, 6],
        [3, 6, 5, 9, 7, 1, 2, 4, 8],
        [5, 4, 7, 1, 9, 3, 6, 8, 2],
        [9, 3, 6, 7, 2, 8, 1, 5, 4],
        [2, 1, 8, 5, 4, 6, 7, 3, 9],
        [8, 2, 3, 4, 1, 9, 0, 6, 7],
        [6, 9, 4, 3, 5, 7, 8, 2, 1],
        [7, 5, 1, 8, 6, 2, 4, 9, 0] 
    ]
    assert(not verifySolution(testSquareDuplicates))
    print("Testing correct1")
    testCorrect = [
        [1, 8, 2, 6, 3, 4, 9, 7, 5],
        [4, 7, 9, 2, 8, 5, 3, 1, 6],
        [3, 6, 5, 9, 7, 1, 2, 4, 8],
        [5, 4, 7, 1, 9, 3, 6, 8, 2],
        [9, 3, 6, 7, 2, 8, 1, 5, 4],
        [2, 1, 8, 5, 4, 6, 7, 3, 9],
        [8, 2, 3, 4, 1, 9, 5, 6, 7],
        [6, 9, 4, 3, 5, 7, 8, 2, 1],
        [7, 5, 1, 8, 6, 2, 4, 9, 3]
    ]
    assert(verifySolution(testCorrect))
    print("Testing correct2")
    testCorrect2 = [
        [9, 1, 5, 2, 3, 4, 6, 7, 8],
        [4, 7, 2, 8, 5, 6, 3, 1, 9],
        [3, 8, 6, 9, 7, 1, 2, 4, 5],
        [7, 9, 1, 4, 6, 2, 5, 8, 3],
        [2, 6, 3, 1, 8, 5, 7, 9, 4],
        [5, 4, 8, 7, 9, 3, 1, 6, 2],
        [8, 3, 7, 6, 2, 9, 4, 5, 1],
        [6, 5, 4, 3, 1, 8, 9, 2, 7],
        [1, 2, 9, 5, 4, 7, 8, 3, 6]
    ]
    assert(verifySolution(testCorrect2))
    print("Testing correct3")
    testCorrect3 = [
        [9, 5, 2, 4, 7, 1, 3, 6, 8],
        [1, 6, 7, 5, 3, 8, 9, 4, 2],
        [4, 8, 3, 2, 6, 9, 1, 7, 5],
        [7, 1, 6, 8, 5, 4, 2, 3, 9],
        [5, 4, 8, 3, 9, 2, 6, 1, 7],
        [3, 2, 9, 7, 1, 6, 5, 8, 4],
        [8, 9, 4, 6, 2, 3, 7, 5, 1],
        [2, 3, 5, 1, 4, 7, 8, 9, 6],
        [6, 7, 1, 9, 8, 5, 4, 2, 3]
    ]
    assert(verifySolution(testCorrect3))

def test():
    testHasDuplicates()
    testVerifySolution()

if __name__ == "__main__":
    test()