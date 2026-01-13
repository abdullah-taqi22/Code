import random

print("🎮 Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Enter your guess (or type 'q' to quit): ")

    if guess.lower() == 'q':
        print("Game exited. The number was:", number)
        break

    if not guess.isdigit():
        print("❌ Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < number:
        print("📉 Too low!")
    elif guess > number:
        print("📈 Too high!")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
