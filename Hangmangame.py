import random

# Predefined list of 5 words
words = ["python", "puzzle", "guitar", "planet", "shadow"]

# Randomly select a secret word
secret_word = random.choice(words)

# Game state tracking
guessed_letters = []
incorrect_guesses_remaining = 6

print("Welcome to Hangman!")
print(f"The word has {len(secret_word)} letters. You have 6 incorrect guesses allowed.\n")

# Main game loop
while incorrect_guesses_remaining > 0:
    # Build the masked word display (e.g., "p _ t h _ n")
    display_word = []
    for letter in secret_word:
        if letter in guessed_letters:
            display_word.append(letter)
        else:
            display_word.append("_")
            
    print("Word:", " ".join(display_word))
    print(f"Guesses left: {incorrect_guesses_remaining}")
    print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

    # Check for a win condition (no underscores left)
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word correctly!")
        break

    # Get player input
    guess = input("\nGuess a letter: ").strip().lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.\n")
        continue

    # Record the guess
    guessed_letters.append(guess)

    # Check if the guess is in the secret word
    if guess in secret_word:
        print(f"Good job! '{guess}' is in the word.\n")
    else:
        incorrect_guesses_remaining -= 1
        print(f"Sorry, '{guess}' is not in the word.\n")

# Loss condition check
if incorrect_guesses_remaining == 0:
    print(f"Game Over! You ran out of guesses. The word was '{secret_word}'.")