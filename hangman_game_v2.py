import random

word_list = ["apple", "banana", "orange", "grape", "mango"]
secret_word = random.choice(word_list)

guessed_letters = []
max_incorrect_guesses = 6
incorrect_guesses = 0
def display_word():
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()
print("Welcome to Hangman!")
while incorrect_guesses < max_incorrect_guesses and "_" in display_word():
    print("\nWord: ", display_word())
    print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

if "_" not in display_word():
    print("\nCongratulations! You guessed the word:", secret_word)
else:
    print("\nGame Over! The word was:", secret_word)
