import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_MISTAKES = len(STAGES) - 1  # 5


def get_random_word():
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    print("-" * 30)
    print(STAGES[mistakes])
    display_word = " ".join(
        letter if letter in guessed_letters else "_" for letter in secret_word
    )
    print(f"Word:    {display_word}")
    print(f"Mistakes: {mistakes}/{MAX_MISTAKES}")
    print(f"Guessed: {', '.join(sorted(guessed_letters)) or '-'}")
    print("-" * 30)


def get_valid_input(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character!")
        elif guess in guessed_letters:
            print("You already guessed that letter!")
        else:
            return guess


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("\nWelcome to Snowman Meltdown! ⛄")

    while mistakes < MAX_MISTAKES:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = get_valid_input(guessed_letters)

        if guess in secret_word:
            guessed_letters.append(guess)
            print("✅ Correct!")
        else:
            mistakes += 1
            print(f"❌ Wrong!")

        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"🎉 You saved the snowman! The word was: {secret_word}")
            return

    display_game_state(mistakes, secret_word, guessed_letters)
    print(f"😢 The snowman melted! The word was: {secret_word}")


def main():
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").lower().strip()
        if again not in ("yes", "y"):
            print("Thanks for playing! Goodbye! 👋")
            break


if __name__ == "__main__":
    main()