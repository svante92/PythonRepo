# author: Svante Aretun
# date: 1/23/23
# file: hangman.py is a program that allows the user to play the game hangman
# input: User selects the game options (word length and number of lives). The user also guesses letters that are in the hidden target word.
# output: Outputs whether a user has guessed a correct letter, guessed the word, or ran out of guesses

from random import choice, random, randint
from sys import exit

dictionary_file = "dictionary.txt"   # make a dictionary.txt in the same folder where hangman.py is located


# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

def import_dictionary (filename) :
    dictionary = {}
    max_size = 12
    try :
        fh = open(filename, 'r')
        for line in fh:
            word = line.strip()
            size = len(word)
            if size < max_size and size > 0:
                if size not in dictionary.keys():
                    dictionary[size] = []
                dictionary.get(size).append(word.lower())
        fh.close
    except:
        print('An error occurred while opening a file.')
    return dictionary

# print the dictionary (use only for debugging)
def print_dictionary (dictionary) :
    max_size = 12
    print(dictionary)

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options () :
    try:
        size = int(input('Please choose a size of a word to be guessed [3 - 12, default any size]:\n'))
        if size > 12 or size < 3:
                size = randint(3, 12)
                print(f'The word size is set to {size}.')
        else:
            print(f'The word size is set to {size}.')
    except:
        size = randint(3, 12)
        print(f'The word size is set to {size}.')

    try:
        lives = int(input('Please choose a number of lives [1 - 10, default 5]:\n'))
        if lives > 10 or lives < 1:
            lives = 5
        print(f'You have {lives} lives.')
    except:
        lives = 5
        print(f'You have {lives} lives.')

    return (size, lives)

# MAIN
if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print the dictionary (use only for debugging)
    #print_dictionary(dictionary)

    # print a game introduction
    print('Welcome to the Hangman Game!')

    # START GAME
    while True:
    # set up game options (the word size and number of lives)
        size, lives = get_game_options()

        # select a word from a dictionary (according to the game options)
        myList = dictionary.get(size)
        word = choice(myList)
        lettersChosen = []
        lettersChosenDisplay = ''
        print(f'Letters chosen: {lettersChosenDisplay}')
        hiddenWord = []
        for i in range(len(word)):
            curr = word[i]
            if curr == '-':
                hiddenWord.append('-')
            else:
                hiddenWord.append('__')

        hiddenWordDisplay = hiddenWord[0] + ' '
        for i in range(1, size - 1):
            hiddenWordDisplay += ' ' + hiddenWord[i] + ' '
        hiddenWordDisplay += ' ' + hiddenWord[size - 1]

        livesDisplay = 'O' * lives
        livesLost = 0
        print(hiddenWordDisplay + "   lives: " + str(lives) + " " + livesDisplay)

        # START GAME LOOP   (INNER PROGRAM LOOP)
        while True:
            # format and print the game interface:
            # Letters chosen: E, S, P                list of chosen letters
            # __ P P __ E    lives: 4   XOOOO        hidden word and lives
            # ask the user to guess a letter
            while True:
                guess = input('Please choose a new letter >\n')
                if guess.lower() in lettersChosen:
                    print('You have already chosen this letter.')
                elif type(guess) == str:
                    if len(guess) == 1:
                        if guess.isalpha():
                            break
            # update the list of chosen letters
            lettersChosen.append(guess)
            # if the letter is correct update the hidden word,
            if word.__contains__(guess.lower()):
                for i in range(len(word)):
                    if word[i] == guess.lower():
                        hiddenWord[i] = guess.upper()

            # else update the number of lives
            # and print interactive messages
            else:
                lives -= 1
                livesLost += 1
                livesDisplay = 'X' * livesLost + 'O' * lives
            if word.__contains__(guess.lower()):
                print('You guessed right!')
            else:
                print('You guessed wrong, you lost one life.')

            hiddenWordDisplay = hiddenWord[0] + ' '
            for i in range(1, size - 1):
                hiddenWordDisplay += ' ' + hiddenWord[i] + ' '
            hiddenWordDisplay += ' ' + hiddenWord[size - 1]

            lettersChosenDisplay = lettersChosen[0].upper()

            if len(lettersChosen) > 1:
                for i in range(1, len(lettersChosen)-1):
                    lettersChosenDisplay += ', ' + lettersChosen[i].upper()
                lettersChosenDisplay += ', ' + lettersChosen[len(lettersChosen)-1].upper()

            print(f'Letters chosen: {lettersChosenDisplay}')
            print(hiddenWordDisplay + "   lives: " + str(lives) + " " + livesDisplay)

            # check if the user guesses the word correctly or lost all lives,
            doExit = False
            if lives == 0:
                doExit = True
                print(f'You lost! The word is {word.upper()}!')
                while True:
                    playAgain = str(input('Would you like to play again [Y/N]?\n'))
                    if playAgain.upper() == 'N':
                        break
                    elif playAgain.upper() == 'Y':
                        break

            if '__' not in hiddenWord:
                doExit = True
                print(f'Congratulations!!! You won! The word is {word.upper()}!')
                # ask if the user wants to continue playing,
                # if yes start a new game, otherwise terminate the program
                while True:
                    playAgain = str(input('Would you like to play again [Y/N]?\n'))
                    if playAgain.upper() == 'N':
                        break
                    elif playAgain.upper() == 'Y':
                        break
            if doExit:
                break

        # END GAME
        if playAgain.upper() == 'N':
            print("\nGoodbye!")
            exit()

