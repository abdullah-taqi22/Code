import random

points = 100

print("🎲 DICE ROLLING BETTING GAME 🎲")
print("You start with 100 points")

while points > 0:
    print("\n--------------------------")
    print(f"Your points: {points}")
    print("Bet options:")
    print("1️⃣ Low (2–6)")
    print("2️⃣ Mid (7)")
    print("3️⃣ High (8–12)")
    print("Q️⃣ Quit")

    choice = input("Choose your bet: ").lower()

    if choice == 'q':
        break

    if choice not in ['1', '2', '3']:
        print("❌ Invalid choice")
        continue

    bet = input("Enter bet amount: ")

    if not bet.isdigit() or int(bet) <= 0:
        print("❌ Invalid bet")
        continue

    bet = int(bet)

    if bet > points:
        print("❌ Not enough points")
        continue

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    print(f"\n🎲 Dice rolled: {dice1} + {dice2} = {total}")

    win = False

    if choice == '1' and 2 <= total <= 6:
        win = True
    elif choice == '2' and total == 7:
        win = True
    elif choice == '3' and 8 <= total <= 12:
        win = True

    if win:
        points += bet
        print(f"✅ YOU WIN! +{bet} points")
    else:
        points -= bet
        print(f"❌ YOU LOSE! -{bet} points")

if points == 0:
    print("\n💀 GAME OVER — You ran out of points")

print(f"\n🏁 Final Points: {points}")
print("Thanks for playing 🎲")
