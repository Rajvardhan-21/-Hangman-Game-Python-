import random

words = ["python", "computer", "programming", "database", "datascience"]

word = random.choice(words)
guessed = []
attempts = 6

print("🎮 Welcome to Hangman!")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Attempts left:", attempts)

    if "_" not in display:
        print("🎉 You won!")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter!")
        continue

    guessed.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        print("❌ Wrong guess!")
        attempts -= 1

else:
    print("\n💀 Game Over!")
    print("The word was:", word)
