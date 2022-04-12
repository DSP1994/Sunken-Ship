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


def get_random_word(list_of_words):
    # a function that returns a random word from the above list
    letter_index = random.randint(0, len(list_of_words) - 1)
    return list_of_words[letter_index]


def game_overview(characters_omitted, characters_found, mystery_string):
    print(SUNKEN_SHIP_PICS[len(characters_omitted)])
    print()
    print('Missed letters:', end=' ')
    for letter in characters_omitted:
        print(letter, end=' ')
    print()
    blanks = '_' * len(mystery_string)
    for i in range(len(mystery_string)): 
        # Replace blanks with correctly guessed letters.
        if mystery_string[i] in characters_found:
            blanks = blanks[:i] + mystery_string[i] + blanks[i+1:]
    for letter in blanks: 
        # Show the secret word with spaces in between each letter.
        print(letter, end=' ')
    print()


def recieve_player_guess(previously_recieved):
    # Returns the letter the player guessed. Also ensures
    # the player enters a single letter, nothing else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()  # this will turn even an uppercase into lower
        if len(guess) != 1:  # checks if one character long (ie a letter)
            print('Please enter a single letter.')
        elif guess in previously_recieved:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def do_you_want_to_play_again():
    # Function that returns True if player wants to play again.
    # otherwise returns as false.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


# Is the title of the game
print('S U N K E N   S H I P')

# will be blank until the player has guessed some letters.
characters_omitted = ''

# same as above.
characters_found = ''

# won't be displayed to the user
mystery_string = get_random_word(words)

# will only be set to true when it's been given a signal by the user
# that they want to play again.
is_sunken_ship_finished = False


# calls the displayBoard function, giving it three variables
while True:
    game_overview(characters_omitted, characters_found, mystery_string)
    # lets the player enter a letter
    guess = recieve_player_guess(characters_omitted + characters_found)
    if guess in mystery_string:
        characters_found = characters_found + guess

        # checking if the player has won, needs to check every letter
        # in every position to ensure win. ie 1 letter could be in 2
        # different locations.
        all_characters_guessed = True
        for i in range(len(mystery_string)):
            if mystery_string[i] not in characters_found:
                all_characters_guessed = False
                break
        if all_characters_guessed:
            print('Yes! The secret word is "' 
            + mystery_string + '"! You have won!')
            is_sunken_ship_finished = True
    else:
        characters_omitted = characters_omitted + guess
        # check if the player has guessed too many times and lost.
        if len(characters_omitted) == len(SUNKEN_SHIP_PICS) - 1:
            game_overview(characters_omitted, characters_found, mystery_string)
            print('You have run out of guesses!\nAfter '
              + str(len(characters_omitted)) + ' missed guesses and '
              + str(len(characters_found)) + ' correct guesses, the word was "'
              + mystery_string + '"')
            is_sunken_ship_finished = True
    
    # Asking the player if they wish to try again.
    # (but only if the game is done).
    if is_sunken_ship_finished:
        if do_you_want_to_play_again():
            characters_omitted = ''
            characters_found = ''
            is_sunken_ship_finished = False
            mystery_string = get_random_word(words)
        else:
            break