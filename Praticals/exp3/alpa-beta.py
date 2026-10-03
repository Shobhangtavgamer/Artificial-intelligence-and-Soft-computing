import math
board = [" " for _ in range(9)]
def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()
def print_positions():
    print("\nBoard Positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()
def is_winner(player):
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for line in wins:
        if all(board[i] == player for i in line):
            return True
    return False
def is_draw():
    return " " not in board
def minimax(depth, maximizing, alpha, beta):
    # Computer wins
    if is_winner("O"):
        return 10 - depth
    # User wins
    if is_winner("X"):
        return depth - 10
    # Draw
    if is_draw():
        return 0
    # Maximizing player = Computer O
    if maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(
                    depth + 1,
                    False,
                    alpha,
                    beta
                )
                board[i] = " "
                best = max(best, score)
                # Alpha update
                alpha = max(alpha, best)
                # Alpha-Beta pruning
                if beta <= alpha:
                    break
        return best
    # Minimizing player = User X
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(
                    depth + 1,
                    True,
                    alpha,
                    beta
                )
                board[i] = " "
                best = min(best, score)
                # Beta update
                beta = min(beta, best)
                # Alpha-Beta pruning
                if beta <= alpha:
                    break
        return best
def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(
                0,
                False,
                -math.inf,
                math.inf
            )
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move
def play_game():
    global board
    board = [" " for _ in range(9)]
    print("\n==============================")
    print("     TIC TAC TOE")
    print(" Alpha-Beta Pruning AI")
    print("==============================")
    print_positions()
    print("You are X")
    print("Computer is O")
    while True:
        print_board()
        while True:
            try:
                position = int(
                    input("Enter your position (1-9): ")
                )
                if position < 1 or position > 9:
                    print("Please enter a number from 1 to 9.")
                    continue
                index = position - 1
                if board[index] != " ":
                    print("Position already occupied.")
                    continue
                board[index] = "X"
                break
            except ValueError:
                print("Please enter a valid number.")
        # Check user win
        if is_winner("X"):
            print_board()
            print("Congratulations! You won!")
            break
        # Check draw
        if is_draw():
            print_board()
            print("Game Draw!")
            break
        print("\nComputer is thinking...")
        computer_move = best_move()
        board[computer_move] = "O"
        print(
            f"Computer selected position: "
            f"{computer_move + 1}"
        )
        # Check computer win
        if is_winner("O"):
            print_board()
            print("Computer wins!")
            break
        # Check draw
        if is_draw():
            print_board()
            print("Game Draw!")
            break
while True:
    play_game()
    choice = input(
        "\nDo you want to play again? (y/n): "
    ).lower()
    if choice != "y":
        print("\nThank you for playing!")
        break