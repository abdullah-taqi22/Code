import os
import time
import random

road_width = 5
player_pos = road_width // 2
enemy_pos = random.randint(0, road_width - 1)
score = 0
speed = 0.4

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_road(player, enemy, score):
    for row in range(10):
        line = ""
        for col in range(road_width):
            if row == 8 and col == player:
                line += "🚗"
            elif row == 2 and col == enemy:
                line += "🚙"
            else:
                line += "⬛"
        print(line)
    print(f"\nScore: {score}")
    print("A = Left | D = Right | Q = Quit")

while True:
    clear()
    draw_road(player_pos, enemy_pos, score)

    move = input("Move: ").lower()

    if move == 'a' and player_pos > 0:
        player_pos -= 1
    elif move == 'd' and player_pos < road_width - 1:
        player_pos += 1
    elif move == 'q':
        print("Game Quit 🚫")
        break

    if enemy_pos == player_pos:
        clear()
        print("💥 CRASH!")
        print(f"Final Score: {score}")
        break

    score += 1
    enemy_pos = random.randint(0, road_width - 1)
    speed = max(0.1, speed - 0.01)
    time.sleep(speed)
