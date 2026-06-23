import random

player_name = ""
player_score = 0
ai_score = 0
draws = 0
history = []

def create_board():
    return [" " for _ in range(9)]

def display_board(board):
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---+---+---")
    print()

def check_winner(board, symbol):

    patterns = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for pattern in patterns:
        if all(board[i] == symbol for i in pattern):
            return True

    return False

def board_full(board):
    return " " not in board

def player_move(board):

    while True:

        try:
            move = int(input("Enter position (1-9): ")) - 1

            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break

            print("Invalid Move!")

        except:
            print("Enter a valid number!")

def ai_move(board):

    # Win if possible
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            if check_winner(board, "O"):
                return

            board[i] = " "

    # Block player
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"

            if check_winner(board, "X"):
                board[i] = "O"
                return

            board[i] = " "

    available = [i for i in range(9) if board[i] == " "]
    board[random.choice(available)] = "O"

def play_game():

    global player_score
    global ai_score
    global draws

    board = create_board()

    while True:

        display_board(board)

        player_move(board)

        if check_winner(board, "X"):
            display_board(board)

            print(f"🏆 {player_name} Wins!")
            player_score += 1
            history.append("Player Won")
            break

        if board_full(board):
            display_board(board)

            print("🤝 Draw Match")
            draws += 1
            history.append("Draw")
            break

        ai_move(board)

        if check_winner(board, "O"):
            display_board(board)

            print("🤖 AI Wins!")
            ai_score += 1
            history.append("AI Won")
            break

        if board_full(board):
            display_board(board)

            print("🤝 Draw Match")
            draws += 1
            history.append("Draw")
            break

def statistics():

    total = player_score + ai_score + draws

    print("\n========== STATISTICS ==========")
    print("Player Wins :", player_score)
    print("AI Wins     :", ai_score)
    print("Draws       :", draws)

    if total > 0:
        print("Win Rate    :", round((player_score/total)*100, 2), "%")

def show_history():

    print("\n========== MATCH HISTORY ==========")

    if not history:
        print("No Matches Played")
        return

    for i, result in enumerate(history, start=1):
        print(f"Match {i}: {result}")

print("""
========================================
      TIC-TAC-TOE AI CHAMPIONSHIP
========================================
""")

player_name = input("Enter Player Name: ")

while True:

    print("""
1. Play Match
2. Statistics
3. Match History
4. Exit
""")

    choice = input("Enter Choice: ")

    if choice == "1":
        play_game()

    elif choice == "2":
        statistics()

    elif choice == "3":
        show_history()

    elif choice == "4":
        print("Thank You For Playing!")
        break

    else:
        print("Invalid Choice!")