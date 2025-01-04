# Function to check if it's safe to place a number at a given position
def is_safe(board, row, col, num):
    # Check if the number is already in the row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check if the number is already in the column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check if the number is already in the 3x3 sub-grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    
    return True

# Function to solve the Sudoku board using backtracking
def solve_sudoku(board):
    # Find the next empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try placing numbers 1 to 9
                for num in range(1, 10):
                    if is_safe(board, row, col, num):
                        board[row][col] = num
                        
                        # Recursively attempt to solve the rest of the board
                        if solve_sudoku(board):
                            return True
                        
                        # If no solution, backtrack
                        board[row][col] = 0
                return False
    return True

# Function to print the Sudoku board
def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))

# Example Sudoku board (0 represents an empty space)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku and print the result
if solve_sudoku(sudoku_board):
    print("Solved Sudoku:")
    print_board(sudoku_board)
else:
    print("No solution exists")
