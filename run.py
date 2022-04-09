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

displayBoard()