import random
SUNKEN_SHIP_PICS = [
    # The capital letters indicate that this is
    # not to be changed, under any circumstances.
    """
      /|\\
     /_|_\\
   ____|____
   \_o_o_o_/
~~   |       ~~~~~
     t
    """, """
      /|\\
     /_|_\\
   ____|____
   \_o_o_o_/
~~   |       ~~~~~
    """, """
      /|\\
     /_|_\\
   ____|____
   \_o_o_o_/
~~~         ~~~~~~
    """, """
      /|\\
     /_|_\\
   ____|____
~~~         ~~~~~~
    """, """
      /|\\
     /_|_\\
~~~~~     ~~~~~~~~
    """, """
      /|\\
~~~~~~   ~~~~~~~~~
    """, """
~~~~~~~~~~~~~~~~~~ """]

words = 'clam crab manatee turtle cuttlefish prawn\
        sponge shrimp squid lobster mackerel seal hammerhead\
        sealion marlin pufferfish octopus dolphin sunfish seahorse\
        stringray eagleray whaleshark clownfish starfish toadfish'.split()


def get_random_word(word_list):
    # a function that returns a random word from the above list
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]


def display_board(missed_letters, correct_letters, secret_word):
    print(SUNKEN_SHIP_PICS[len(missed_letters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
        # Replaces the blanks with correctly guessed letters
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:
        # Shows the secret word with spaces between each letter
        print(letter, end=' ')
    print()


def get_guess(already_guessed):
    # Returns the letter the player guessed. Also ensures
    # the player enters a single letter, nothing else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()  # this will turn even an uppercase into lower
        if len(guess) != 1:  # checks if one character long (ie a letter)
            print('Please enter a single letter')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def play_again():
    # Function that returns True if player wants to play again.
    # otherwise returns as false.
    print('Do you want to go again? (yes or no)')
    return input().lower().startswith('y')


# Is the title of the game
print('S U N K E N S H I P')
# will be blank until the player has guessed some letters.
missed_letters = ''
# same as above.
correct_letters = ''
# won't be displayed to the user
secret_word = get_random_word(words)
# will only be set to true when it's been given a signal by the user
# that they want to play again.
game_is_done = False

# calls the displayBoard function, giving it three variables
while True:
    display_board(missed_letters, correct_letters, secret_word)
    # lets the player enter a letter
    guess = get_guess(missed_letters + correct_letters)
    if guess in secret_word:
        correct_letters = correct_letters + guess

        # checking if the player has won, needs to check every letter
        # in every position to ensure win. ie 1 letter could be in 2
        # different locations.
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
            if found_all_letters:
                print('Yes!! The secret word was "' +
                      secret_word + '"! You won!')
                game_is_done = True
        else:
            missed_letters = missed_letters + guess

            # check if the player has guessed too many times and lost.
            if len(missed_letters) == len(SUNKEN_SHIP_PICS) - 1:
                display_board(missed_letters, correct_letters, secret_word)
                print('You have run out of guesses!\nAfter ' +
                      str(len(missed_letters)) + ' missed guesses and ' +
                      str(len(correct_letters)) + ' correct guesses, \
                            the word was "' + secret_word + '"')
                game_is_done = True

            # Asking the player if they wish to try again.
            # (but only if the game is done).
            if game_is_done:
                if play_again():
                    missed_letters = ''
                    correct_letters = ''
                    game_is_done = False
                    secret_word = get_random_word(words)
                else:
                    break
