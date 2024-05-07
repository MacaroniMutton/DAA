def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N), range(col, N)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens_util(board, row, N, solutions):
    if row == N:
        solutions.append([row[:] for row in board])
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, N, solutions)
            board[row][col] = 0

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    solutions = []  
    solve_n_queens_util(board, 0, N, solutions)
    return solutions

def main():
    n = 6
    solutions = solve_n_queens(n)
    for solution in solutions:
        for i in range(n):
            print("+---"*n, end="")
            print("+")
            for j in range(n):
                if solution[i][j]==1:
                    print("| Q ", end="")
                else:
                    print("|   ", end="")
            print("|", end="")
            print()
        print("+---"*n, end="")
        print("+")
        print()

    print(f"Total number of solutions: {len(solutions)}")

if __name__=='__main__':
    main()
