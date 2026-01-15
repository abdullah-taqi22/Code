import random

# Word list
words = ["python", "developer", "hangman", "programming", "keyboard"]

word = random.choice(words)
guessed_letters = set()
lives = 6

print("🔤 WELCOME TO HANGMAN 🔤")
print("Guess the word, one letter at a time.")
print("You have 6 lives ❤️")

while lives > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print("Lives left:", lives)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter ONE letter only.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print("✅ Good guess!")
    else:
        print("❌ Wrong guess!")
        lives -= 1

    # Win condition
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 YOU WIN!")
        print("The word was:", word)
        break

# Lose condition
if lives == 0:
    print("\n💀 GAME OVER")
    print("The word was:", word)
