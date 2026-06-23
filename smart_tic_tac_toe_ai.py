import random

player_score = 0
ai_score = 0

board = [" " for _ in range(9)]

def display_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(symbol):

    win_patterns = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for pattern in win_patterns:
        if all(board[i] == symbol for i in pattern):
            return True

    return False

def board_full():
    return " " not in board

def player_move():

    while True:
        try:
            move = int(input("Choose position (1-9): ")) - 1

            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move!")
        except:
            print("Enter numbers only!")

def ai_move():

    # Try to win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner("O"):
                return
            board[i] = " "

    # Block player
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner("X"):
                board[i] = "O"
                return
            board[i] = " "

    # Take center
    if board[4] == " ":
        board[4] = "O"
        return

    # Random move
    available = [i for i in range(9) if board[i] == " "]
    board[random.choice(available)] = "O"

def play_game():

    global player_score, ai_score

    while True:

        for i in range(9):
            board[i] = " "

        print("\n===== NEW MATCH =====")

        while True:

            display_board()

            player_move()

            if check_winner("X"):
                display_board()
                print("🎉 You Win!")
                player_score += 1
                break

            if board_full():
                display_board()
                print("🤝 Draw Match!")
                break

            ai_move()

            if check_winner("O"):
                display_board()
                print("🤖 AI Wins!")
                ai_score += 1
                break

            if board_full():
                display_board()
                print("🤝 Draw Match!")
                break

        print("\n----- SCOREBOARD -----")
        print("Player :", player_score)
        print("AI     :", ai_score)

        again = input("\nPlay Again? (y/n): ").lower()

        if again != "y":
            print("\nThanks for Playing!")
            break

print("""
=================================
      SMART TIC-TAC-TOE AI
=================================
Player Symbol : X
AI Symbol     : O
Positions:

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
=================================
""")

play_game()