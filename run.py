import random
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

words = 'clam crab manatee turtle cuttlefish prawn\
        sponge shrimp squid lobster mackerel seal hammerhead\
        sealion marlin pufferfish octopus dolphin sunfish seahorse\
        stringray eagleray whaleshark clownfish starfish toadfish'.split()


def getRandomWord(wordList):
    # a function that returns a random word from the above list
    wordIndex = random.randinit(0, len(wordList) -1)
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

# Is the title of the game
print('S U N K E N S H I P')
# will be blank until the player has guessed some letters.
missedLetters = ''
# same as above.
correctLetters = ''
# won't be displayed to the user
secretWord = getRandomWord(word)
# will only be set to true when it's been given a signal by the user
# that they want to play again.
gameIsDone = False

# calls the displayBoard function, giving it three variables
while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    #lets the player enter a letter
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess

        #checking if the player has won, needs to check every letter
        #in every position to ensure win. ie 1 letter could be in 2
        #different locations. 
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print('Yes!! The secret word was "' + secretWord + '"! You won!!')
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            #check if the player has guessed too many times and lost.
            if len(missedLetter) == len(SUNKEN_SHIP_PICS) - 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!\nAfter ' + 
                    str(len(missedLetters)) + ' missed guesses and ' +
                    str(len(correctLetters)) + ' correct guesses, the word was "' +
                    secretWord + '"')
                gameIsDone = True
            
            #Asking the player if they wish to try again.
            #(but only if the game is done). 
            if gameIsDone:
                if playAgain():
                    missedLetters = ''
                    correctLetters = ''
                    gameIsDone = False
                    secretWord = getRandomWord(words)