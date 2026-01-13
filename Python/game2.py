import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

print("🎮 Rock Paper Scissors Game")
print("Type rock, paper, or scissors (q to quit)")

while True:
    user = input("\nYour choice: ").lower()

    if user == 'q':
        print("\nGame Over!")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)
        break

    if user not in choices:
        print("❌ Invalid choice. Try again.")
        continue

    computer = random.choice(choices)
    print("🤖 Computer chose:", computer)

    if user == computer:
        print("😐 It's a tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("🎉 You win this round!")
        user_score += 1
    else:
        print("💀 Computer wins this round!")
        computer_score += 1
