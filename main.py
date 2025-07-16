import hangman_words
import hangman_art
import random

lives = 6
print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

placeholder = "_" * word_length
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"\n******** {lives}/6 LIVES LEFT ********")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed the letter '{guess}'")
        continue

    correct_letters.append(guess)

    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")

    print(hangman_art.stages[6 - lives])

    if "_" not in display:
        game_over = True
        print("\n🎉 YOU WIN! 🎉")
    elif lives == 0:
        game_over = True
        print(f"\n💀 YOU LOST 💀 The word was: {chosen_word}")
