import random

# ANSI colors
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def print_board(board):
    def symbol(s):
        if s == "X":
            return RED + "X" + RESET
        elif s == "O":
            return BLUE + "O" + RESET
        else:
            return " "

    print("\n")
    print(f" {symbol(board[0])} {YELLOW}|{RESET} {symbol(board[1])} {YELLOW}|{RESET} {symbol(board[2])} ")
    print(f"{YELLOW}---+---+---{RESET}")
    print(f" {symbol(board[3])} {YELLOW}|{RESET} {symbol(board[4])} {YELLOW}|{RESET} {symbol(board[5])} ")
    print(f"{YELLOW}---+---+---{RESET}")
    print(f" {symbol(board[6])} {YELLOW}|{RESET} {symbol(board[7])} {YELLOW}|{RESET} {symbol(board[8])} ")
    print("\n")

def check_winner(board, player):
    combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(board[a]==board[b]==board[c]==player for a,b,c in combos)

def get_free_positions(board):
    return [i for i in range(9) if board[i] == " "]

def ai_move(board):
    # Try to WIN
    for i in get_free_positions(board):
        board[i] = "O"
        if check_winner(board, "O"):
            board[i] = " "
            return i
        board[i] = " "

    # Try to BLOCK
    for i in get_free_positions(board):
        board[i] = "X"
        if check_winner(board, "X"):
            board[i] = " "
            return i
        board[i] = " "

    # Otherwise random
    return random.choice(get_free_positions(board))

def play_game(vs_ai):
    board = [" "] * 9
    current = "X"

    while True:
        print_board(board)

        if current == "X" or not vs_ai:
            move = input(f"Player {current}, choose (1-9): ")
            if not move.isdigit() or not 1 <= int(move) <= 9:
                print("❌ Invalid move")
                continue
            move = int(move) - 1
            if board[move] != " ":
                print("❌ Position taken")
                continue
        else:
            move = ai_move(board)
            print("🤖 Computer chooses:", move + 1)

        board[move] = current

        if check_winner(board, current):
            print_board(board)
            winner = "Computer 🤖" if vs_ai and current == "O" else f"Player {current}"
            print(f"🎉 {winner} wins!")
            break

        if " " not in board:
            print_board(board)
            print("😐 It's a DRAW!")
            break

        current = "O" if current == "X" else "X"

# MAIN MENU
print("🎮 TIC TAC TOE")
print("1️⃣  Play with Friend")
print("2️⃣  Play with Computer (AI)")

choice = input("Choose option (1 or 2): ")

if choice == "1":
    play_game(vs_ai=False)
elif choice == "2":
    play_game(vs_ai=True)
else:
    print("❌ Invalid choice")
