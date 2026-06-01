import random

words = [
    {
        "word": "python",
        "hint": "Popular programming language"
    },
    {
        "word": "react",
        "hint": "JavaScript library for UI"
    },
    {
        "word": "spring",
        "hint": "Java framework"
    },
    {
        "word": "docker",
        "hint": "Containerization platform"
    },
    {
        "word": "github",
        "hint": "Version control hosting platform"
    }
]

MAX_ATTEMPTS = 6


def play_game():
    selected = random.choice(words)

    word = selected["word"]
    hint = selected["hint"]

    guessed_letters = []
    attempts = MAX_ATTEMPTS
    score = 0

    print("\n===================================")
    print("   DEVELOPER HANGMAN CHALLENGE")
    print("===================================")

    while attempts > 0:

        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(f"\nWord: {display_word}")
        print(f"Attempts Left: {attempts}")
        print(f"Score: {score}")

        choice = input(
            "\nEnter a letter or type 'hint': "
        ).lower()

        if choice == "hint":
            print(f"Hint: {hint}")
            attempts -= 1
            continue

        if len(choice) != 1 or not choice.isalpha():
            print("Enter a single valid letter.")
            continue

        if choice in guessed_letters:
            print("Already guessed.")
            continue

        guessed_letters.append(choice)

        if choice in word:
            print("Correct!")
            score += 10
        else:
            print("Wrong!")
            attempts -= 1

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations!")
            print(f"You guessed the word: {word.upper()}")
            print(f"Final Score: {score}")
            return

    print("\n💀 Game Over")
    print(f"The word was: {word.upper()}")


while True:
    play_game()

    again = input(
        "\nDo you want to play again? (y/n): "
    ).lower()

    if again != "y":
        print("\nThank you for playing!")
        break
