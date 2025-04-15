# Problem Set 2, hangman.py
# Name: ayush
# Collaborators:
# Time spent:

import random 
import string


WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # Check if all letters in the secret word have been guessed
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    word_progress = ""
    for letter in secret_word:
        if letter in letters_guessed:
            word_progress += letter
        else:
            word_progress += "*"
    return word_progress


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    all_letters = string.ascii_lowercase
    available_letters = [letter for letter in all_letters if letter not in letters_guessed]
    return "".join(available_letters)


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.
    """
    guesses_left = 10
    letters_guessed = []
    
    print(f"Welcome to Hangman! The word contains {len(secret_word)} letters.")
    
    # Game loop
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        
        # Get user input
        guess = input("Please guess a letter: ").lower()
        
        # Check for invalid input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess == "!":
            # Help functionality
            if with_help and guesses_left >= 3:
                for letter in secret_word:
                    if letter not in letters_guessed:
                        letters_guessed.append(letter)
                        guesses_left -= 3
                        print(f"Help! You revealed the letter: {letter}")
                        break
            elif with_help:
                print("Sorry, you don't have enough guesses left to use help.")
            continue
        
        # Check if the guess is correct or incorrect
        if guess in letters_guessed:
            print("You already guessed that letter.")
        elif guess in secret_word:
            letters_guessed.append(guess)
            print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
            if has_player_won(secret_word, letters_guessed):
                print("Congratulations, you've won!")
                break
        else:
            letters_guessed.append(guess)
            if guess in 'aeiou':
                guesses_left -= 2  # Vowel penalty
            else:
                guesses_left -= 1  # Consonant penalty
            print(f"Wrong guess: {get_word_progress(secret_word, letters_guessed)}")
            
    if guesses_left == 0:
        print(f"\nSorry, you've run out of guesses. The word was: {secret_word}")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass
