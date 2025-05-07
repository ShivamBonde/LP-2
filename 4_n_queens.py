# Function to check if placing queen at (row, col) is safe
def is_safe(board, row, col, n):
    # Check the column and diagonals for any conflicts
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

# Function to solve N-Queens using Backtracking
def solve_n_queens(n, board, row):
    if row == n:
        print(board)  # Print the board configuration when solution is found
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col  # Place queen
            if solve_n_queens(n, board, row + 1):
                return True
            board[row] = -1  # Backtrack if no solution
    return False

# Driver code for 8-Queens
n = 8  # Size of the board
board = [-1] * n  # Initialize board with -1 (no queens placed)
solve_n_queens(n, board, 0)
