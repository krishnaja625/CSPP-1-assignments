'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secret_word_giv
the user is to guess. This starts up an interactive game of Hangman between
the user and the computer. Be sure you take advantage of the three helper functions,
isWordGuessed, getGuessedWord, and getAvailableLetters,
that you've defined in the previous part.
'''
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
def get_guessed_word(secret_word, letters_guessed):
    """This function returns a string that is comprised of letters and underscores, based on what
    letters in letters_guessed are in secret_word."""
    str1 = ""
    for i in secret_word:
        if i not in letters_guessed:
            str1 += " _"
        else:
            str1 += i
    return str1

def is_word_guessed(secret_word, letters_guessed):
    '''is word guessed? '''
    secret_set = set(secret_word)
    intersect = secret_set.intersection(set(letters_guessed))
    return bool(len(intersect) == len(secret_set))
def get_available_letters(letters_guessed):
    """gives the available letters for guess """
    import string
    a_list = list(string.ascii_lowercase)
    for i in letters_guessed:
        if i in a_list:
            a_list.remove(i)
    return "".join(a_list)

WORD_LIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORD_LIST_FILENAME, 'r')
    # line: string
    line = in_file.readline()
    # WORD_LIST: list of strings
    word_list = line.split()
    print("  ", len(word_list), "words loaded.")
    return word_list

def choose_word(word_list):
    """
    WORD_LIST (list): list of words (strings)

    Returns a word from WORD_LIST at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable WORD_LIST
# so that it can be accessed from anywhere in the program
WORD_LIST = load_words()

def hangman(secret_word_giv):
    '''
    secret_word_giv: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
    letters the secret_word_giv contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
    about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
    partially guessed word so far, as well as letters that the
    user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.'''
    print("Welcome to the game, Hangman! \n")
    print("I am thinking of a word that is", len(secret_word_giv), "letters long.")
    print("Please enter only one guess(letter) per round \n-------------")
    guess_count = 10
    letters_guessed = []
    while guess_count > 0 and (not is_word_guessed(secret_word_giv, letters_guessed)):
        print("You have", guess_count, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        inp_user = input("Please guess a letter:")
        the_guessed_word = get_guessed_word(secret_word_giv, letters_guessed)
        letters_guessed.append(inp_user)
        if inp_user in the_guessed_word:
            the_guessed_word = get_guessed_word(secret_word_giv, letters_guessed)
            print("Oops! You've already guessed that letter:", the_guessed_word)
            print("\n------------")
        elif inp_user in secret_word_giv:
            #letters_guessed.append(inp_user)
            the_guessed_word = get_guessed_word(secret_word_giv, letters_guessed)
            print("Good guess", the_guessed_word)
            print("\n------------")
            #guess_count -= 1
        elif inp_user not in secret_word_giv:
            #letters_guessed.append(inp_user)
            the_guessed_word = get_guessed_word(secret_word_giv, letters_guessed)
            print("Oops! That letter is not in my word:", the_guessed_word)
            print("\n------------")
            guess_count -= 1
    if is_word_guessed(secret_word_giv, letters_guessed):
        print("Congratulations, you won!")
        print("\n------------")
    else:
        print("Sorry, you ran out of guesses. The word was " + secret_word_giv + "\n------------")
def main():
    '''
    Main function for the given program
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secret_word_giv while you're testing)
    '''
    secret_word_giv = choose_word(WORD_LIST).lower()
    #secret_word_giv = "nani"
    hangman(secret_word_giv)


if __name__ == "__main__":
    main()
