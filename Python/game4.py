import random

print("⚽ PLAYER vs AI PENALTY SHOOTOUT 🤖")
print("Directions: L = Left | C = Center | R = Right")
print("-" * 45)

choices = ['L', 'C', 'R']
player_score = 0
ai_score = 0
shots = 5

def player_shot():
    while True:
        choice = input("Shoot (L/C/R): ").upper()
        if choice in choices:
            return choice
        print("❌ Invalid choice!")

def ai_choice():
    return random.choice(choices)

# Normal penalties
for i in range(1, shots + 1):
    print(f"\n--- PENALTY {i} ---")

    # Player shoots
    player = player_shot()
    ai = ai_choice()
    print(f"🤖 AI dives: {ai}")

    if player != ai:
        print("🥅 GOOOOAL!")
        player_score += 1
    else:
        print("🧤 SAVED!")

    # AI shoots
    print("\n🤖 AI is shooting...")
    ai_shoot = ai_choice()
    player_dive = player_shot()
    print(f"🤖 AI shoots: {ai_shoot}")

    if ai_shoot != player_dive:
        print("❌ AI SCORES!")
        ai_score += 1
    else:
        print("🧤 GREAT SAVE!")

    print(f"\nScore: You {player_score} | AI {ai_score}")

# Sudden Death
round_sd = 1
while player_score == ai_score:
    print(f"\n🔥 SUDDEN DEATH ROUND {round_sd} 🔥")

    player = player_shot()
    ai = ai_choice()
    print(f"🤖 AI dives: {ai}")
    p_goal = player != ai

    ai_shoot = ai_choice()
    player_dive = player_shot()
    print(f"🤖 AI shoots: {ai_shoot}")
    ai_goal = ai_shoot != player_dive

    if p_goal:
        player_score += 1
        print("🥅 YOU SCORE!")
    else:
        print("❌ YOU MISS!")

    if ai_goal:
        ai_score += 1
        print("❌ AI SCORES!")
    else:
        print("🧤 YOU SAVE!")

    if p_goal != ai_goal:
        break

    round_sd += 1

# Final result
print("\n🏁 MATCH OVER")
print(f"FINAL SCORE: You {player_score} | AI {ai_score}")

if player_score > ai_score:
    print("🏆 YOU WIN!")
else:
    print("🤖 AI WINS!")
