def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False

    return True
def solve(board, row, n):
    if row == n:

        print("\nSolution Found:\n")

        for i in range(n):
            for j in range(n):
                if board[i] == j:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        print("\nQueen Positions:")
        for i in range(n):
            print("Row", i + 1, "-> Column", board[i] + 1)
        return True
    for col in range(n):

        if is_safe(board, row, col, n):

            board[row] = col

            if solve(board, row + 1, n):
                return True
            board[row] = -1

    return False

n = int(input("Enter Number of Queens: "))
board = [-1] * n
if not solve(board, 0, n):
    print("\nNo Solution Exists.")