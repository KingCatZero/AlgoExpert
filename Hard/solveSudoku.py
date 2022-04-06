def solveSudoku(board):
    solutions = []
    solveSudokuHelper(board, solutions)
    return solutions[0]

def solveSudokuHelper(board, solutions):    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                for n in range(1, 10):
                    if isPossible(board, n, i, j):
                        newBoard = copyBoard(board)
                        newBoard[i][j] = n
                        solveSudokuHelper(newBoard, solutions)
                        
                    board[i][j] = 0
                        
                return
    
    solutions.append(board)
    
def copyBoard(board):
    return [row[:] for row in board]

def isPossible(board, n, i, j):
    return not (inColumn(board, n, j) or inRow(board, n, i) or inSquare(board, n, i, j))

def inColumn(board, n, j):
    for i in range(len(board)):
        if board[i][j] == n:
            return True
        
    return False

def inRow(board, n, i):
    for j in range(len(board[0])):
        if board[i][j] == n:
            return True
        
    return False

def inSquare(board, n, i, j):
    rowStart = (i // 3) * 3
    colStart = (j // 3) * 3
    
    for i in range(rowStart, rowStart + 3):
        for j in range(colStart, colStart + 3):
            if board[i][j] == n:
                return True
            
    return False
