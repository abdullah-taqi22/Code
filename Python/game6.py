import os
import random

WIDTH = 20
HEIGHT = 10

PLAYER = "👤"
TREE = "🌳"
TREASURE = "💎"
EMPTY = "⬜"

player_x = WIDTH // 2
player_y = HEIGHT // 2
score = 0

# Create map
world = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Add trees
for _ in range(25):
    x = random.randint(0, WIDTH - 1)
    y = random.randint(0, HEIGHT - 1)
    world[y][x] = TREE

# Add treasures
for _ in range(5):
    x = random.randint(0, WIDTH - 1)
    y = random.randint(0, HEIGHT - 1)
    world[y][x] = TREASURE

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def draw_world():
    clear()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x == player_x and y == player_y:
                print(PLAYER, end="")
            else:
                print(world[y][x], end="")
        print()
    print(f"\n💰 Treasures Collected: {score}")
    print("Move: W A S D | Quit: Q")

while True:
    draw_world()
    move = input("Your move: ").lower()

    new_x, new_y = player_x, player_y

    if move == "w":
        new_y -= 1
    elif move == "s":
        new_y += 1
    elif move == "a":
        new_x -= 1
    elif move == "d":
        new_x += 1
    elif move == "q":
        print("👋 Game exited")
        break

    if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT:
        if world[new_y][new_x] != TREE:
            if world[new_y][new_x] == TREASURE:
                score += 1
                world[new_y][new_x] = EMPTY
            player_x, player_y = new_x, new_y

