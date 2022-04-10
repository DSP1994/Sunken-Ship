import random
from pprint import pprint
SUNKEN_SHIP_PICS = [
    # The capital letters indicate that this is
    # not to be changed, under any circumstances.
"""
      /|\
     /_|_\
   ____|____
   \_o_o_o_/
~~   |       ~~~~~
     t
""",
"""
      /|\
     /_|_\
   ____|____
   \_o_o_o_/
~~   |       ~~~~~
""", 
"""
      /|\
     /_|_\
   ____|____
   \_o_o_o_/
~~~         ~~~~~~
""", 
"""
      /|\
     /_|_\
   ____|____
~~~         ~~~~~~
""", 
"""
      /|\
     /_|_\
~~~~~     ~~~~~~~~
""", 
"""
      /|\ 
~~~~~~   ~~~~~~~~~
""", """
~~~~~~~~~~~~~~~~~~
"""]

words = 'clam crab manatee turtle cuttlefish prawn \
        sponge shrimp squid lobster mackerel seal hammerhead \
        sealion marlin pufferfish octopus dolphin sunfish seahorse \
        stringray eagleray whaleshark clownfish starfish toadfish'.split()

def getRandomWord(wordList):
    # a function that returns a random word from the above list
    wordIndex = random,randinit(0, len(wordList) -1)
    return wordList[wordIndex]

def diplayBoard(missingLetters, correctLetters, secretWord):
    print(SUNKEN_SHIP_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        # Replaces the blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        #Shows the secret word with spaces between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player guessed. Also ensures
    # the player enters a single letter, nothing else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower() # this will turn even an uppercase into lower
        if len(guess) != 1: #checks if one character long (ie a letter)
            print('Please enter a single letter')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # Function that returns True if player wants to play again.
    # otherwise returns as false. 
    print('Do you want to go again? (yes or no)')
    return input().lower().startswith('y')

print('S U N K E N S H I P')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(word)
gameIsDone = False

