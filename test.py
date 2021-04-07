import main
def testHasDuplicates(): 
    print("Testing hasDuplicates()...")
    print("\tTesting no duplicates")
    noDuplicates = [1, 2, 3]
    assert(not main.hasDuplicates(noDuplicates))
    print("\tTesting duplicates")
    duplicates = [1, 2, 1]
    assert(main.hasDuplicates(duplicates))
    print("")

def testIsSolved():
    #last row has two -1's
    print("Testing isSolved()...")
    print("\tTesting row duplicates")
    testRowDuplicates = [
        [1, 8, 2, 6, 3, 4, 9, 7, 5],
        [4, 7, 9, 2, 8, 5, 3, 1, 6],
        [3, 6, 5, 9, 7, 1, 2, 4, 8],
        [5, 4, 7, 1, 9, 3, 6, 8, 2],
        [9, 3, 6, 7, 2, 8, 1, 5, 4],
        [2, 1, 8, 5, 4, 6, 7, 3, 9],
        [8, 2, 3, 4, 1, 9, 5, 6, 7],
        [6, 9, 4, 3, 5, 7, 8, 2, 1],
        [-1, 5, 1, 8, 6, 2, 4, 9, -1]
    ]
    print("\tTesting col duplicates")
    assert(not main.isSolved(testRowDuplicates))
    #last column has two -1's
    testColDuplicates = [
        [1, 8, 2, 6, 3, 4, 9, 7, -1],
        [4, 7, 9, 2, 8, 5, 3, 1, 6],
        [3, 6, 5, 9, 7, 1, 2, 4, 8],
        [5, 4, 7, 1, 9, 3, 6, 8, 2],
        [9, 3, 6, 7, 2, 8, 1, 5, 4],
        [2, 1, 8, 5, 4, 6, 7, 3, 9],
        [8, 2, 3, 4, 1, 9, 5, 6, 7],
        [6, 9, 4, 3, 5, 7, 8, 2, 1],
        [7, 5, 1, 8, 6, 2, 4, 9, -1]
    ]
    assert(not main.isSolved(testColDuplicates))
    print("\tTesting square duplicates")
    #bottom right square has two -1's
    testSquareDuplicates = [
        [1, 8, 2, 6, 3, 4, 9, 7, 5],
        [4, 7, 9, 2, 8, 5, 3, 1, 6],
        [3, 6, 5, 9, 7, 1, 2, 4, 8],
        [5, 4, 7, 1, 9, 3, 6, 8, 2],
        [9, 3, 6, 7, 2, 8, 1, 5, 4],
        [2, 1, 8, 5, 4, 6, 7, 3, 9],
        [8, 2, 3, 4, 1, 9, -1, 6, 7],
        [6, 9, 4, 3, 5, 7, 8, 2, 1],
        [7, 5, 1, 8, 6, 2, 4, 9, -1] 
    ]
    assert(not main.isSolved(testSquareDuplicates))
    print("\tTesting incomplete puzzle")
    #bottom right square is 0 (unfilled)
    testIncomplete = [
        [5, 3, 1, 8, 9, 2, 4, 6, 7],
        [6, 2, 9, 7, 4, 3, 1, 8, 5],
        [8, 4, 7, 5, 6, 1, 3, 9, 2],
        [1, 7, 6, 3, 2, 5, 9, 4, 8],
        [2, 9, 3, 4, 8, 6, 7, 5, 1],
        [4, 8, 5, 9, 1, 7, 2, 3, 6],
        [7, 6, 4, 1, 3, 8, 5, 2, 9],
        [9, 1, 8, 2, 5, 4, 6, 7, 3],
        [3, 5, 2, 6, 7, 9, 8, 1, 0]
    ]
    assert(not main.isSolved(testIncomplete))    
    print("\tTesting correct1")
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
    assert(main.isSolved(testCorrect))
    print("\tTesting correct2")
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
    assert(main.isSolved(testCorrect2))
    print("\tTesting correct3")
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
    assert(main.isSolved(testCorrect3))
    print("\tTesting correct4")
    testCorrect4 = [
        [5, 3, 1, 8, 9, 2, 4, 6, 7],
        [6, 2, 9, 7, 4, 3, 1, 8, 5],
        [8, 4, 7, 5, 6, 1, 3, 9, 2],
        [1, 7, 6, 3, 2, 5, 9, 4, 8],
        [2, 9, 3, 4, 8, 6, 7, 5, 1],
        [4, 8, 5, 9, 1, 7, 2, 3, 6],
        [7, 6, 4, 1, 3, 8, 5, 2, 9],
        [9, 1, 8, 2, 5, 4, 6, 7, 3],
        [3, 5, 2, 6, 7, 9, 8, 1, 4]
    ]
    assert(main.isSolved(testCorrect4))

def testGetConstraints():
    print("Testing getConstraints()...")
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0]
    ]
    assert(main.getConstraints(board, 1, 1) == [4, 5, 6, 7, 8, 9])

def printBoard(board):
    for row in board:
        print(row)

def testSolver():
    print("Testing sudoku solver...")
    board = [
        [5, 0, 0, 0, 7, 0, 0, 8, 2],
        [0, 0, 0, 9, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 3, 0],
        [0, 5, 0, 0, 0, 0, 8, 0, 0],
        [6, 7, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 3],
        [0, 0, 4, 3, 5, 0, 0, 0, 0],
        [9, 0, 6, 0, 0, 2, 0, 0, 0],
        [1, 0, 0, 0, 0, 6, 0, 0, 0]
    ]
    print("Testing sudoku1")
    _, solution = main.solve(board)
    printBoard(solution)

    board2 = [
        [8, 2, 0, 0, 0, 0, 6, 0, 0],
        [1, 5, 0, 7, 0, 0, 0, 0, 9],
        [0, 0, 9, 0, 0, 0, 0, 0, 8],
        [6, 8, 1, 5, 0, 7, 0, 9, 4],
        [0, 9, 0, 1, 0, 4, 0, 8, 0],
        [3, 4, 0, 9, 0, 8, 1, 7, 6],
        [5, 0, 0, 0, 0, 0, 8, 0, 0],
        [2, 0, 0, 0, 0, 6, 0, 1, 3],
        [0, 0, 4, 0, 0, 0, 0, 6, 2]
    ]
    print("Testing sudoku2")
    solved, solution2 = main.solve(board2)
    printBoard(solution2)

def test():
    testHasDuplicates()
    testIsSolved()
    testGetConstraints()
    testSolver()

if __name__ == "__main__":
    test()