import random
import listrix   # Yeah, I already regret it.


# Hey, if I'm going to burn out, better sooner rather than later, right?
# Besides, it's not much of a 'secret' word if the program knows it!


guessed_letters = []
spaceman_state = []
wrong_guesses = 0
max_wrong = 15
game_length = 0
letters_complete = 0


# only works for word slot histogram structure
def hist_choice(hotrix, letter_index):
    return random.choices(hotrix[letter_index][0], hotrix[letter_index][1])

def user_input_get():
    # the input function will display a message in the terminal
    # and wait for user input.
    user_in = input()
    return user_in.lower()

def list_item_length(list_in):
    max_len = 0
    for word in list_in:
        if len(word) > max_len:
            max_len = len(word)
    return max_len

def prune_list(list_in, length):
    retlist = list()
    for word in list_in:
        if len(word) == length:
            retlist.append(word)
    return retlist

def decode_nnr(nnr_selection: str):
    return nnr_selection.split('-')

def decode_letter(letter_index):
    return chr(letter_index + 97)

def load_words_list():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')

    max_length = list_item_length(words_list)

    print('Word length? ')
    user_input = user_input_get()
    user_input.strip()

    if int(user_input) not in range(max_length):
        print('Please enter a number between 1 and ' + str(max_length - 2))
        return load_words_list()
    else: 
        global game_length
        game_length = int(user_input)
        return prune_list(words_list, int(user_input))

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    # TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word

    pass


def letter_prompt():
    print('\nPlease guess a letter: ')
    guess = user_input_get()
    global guessed_letters
    if len(guess) == 1:
        if ord(guess) in range(97, 97+26):
            if guess in guessed_letters:
                print('You already guessed "' + guess + '"')
                return letter_prompt()
            else:
                guessed_letters.append(guess)
                return ord(guess) - 97
        else:
            print('\na LETTER you numbskull')
            return letter_prompt()
    else:
        print('\nOne at a time please.')
        return letter_prompt()

def state_gen():
    global spaceman_state
    spaceman_state = []
    for i in range(game_length):
        spaceman_state.append('_ ')

def display_state():
    restr = ''
    for string in spaceman_state:
        restr = restr + string
    print()
    print(restr)
    print()
    print('Guessed letters: ' + str(guessed_letters))

def rebuild_state(nnr_choice, letter_index):
    global spaceman_state
    for slot in decode_nnr(nnr_choice[0]):
        global letters_complete
        letters_complete += 1
        spaceman_state[int(slot)] = decode_letter(letter_index) + ' '

def space_killer(string):
    string.replace(' ', '')
    return string


# Now, this is where you ask, "Wyatt, how can you have a spaceman program that doesn't choose a word?"
# Well, I'll update the comment text when I figure that one out.

def spaceman():

    global guessed_letters
    global spaceman_state
    global wrong_guesses
    global max_wrong
    global game_length
    global letters_complete

    guessed_letters = []
    spaceman_state = []
    wrong_guesses = 0
    max_wrong = 7
    game_length = 0
    letters_complete = 0



    print('''

    ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢

    Our stranded spaceman has found a rocket to get home with. One problem- 
    It's locked! There's a keypad attatched to both a geiger counter, and 
    the lock on the hatch. The pad takes a code word, but he can't reach! 
    Can you help the spaceman crack Schrodingers;Code and get back home? 

    It's exactly as easy as it seems. Good luck, you're going to need it.

    ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢
    
    
    Press Enter to continue, or type 'debug' to enable dev view.

    ''')

    debug = False
    if user_input_get() == 'debug':
        debug = True
    else: 
        debug = False

    # No, I don't know what all this does.
    split_list = load_words_list()
    listr_pre = listrix.list_eater(split_list)
    lstrx = listrix.Listrix3()

    lstrx.explode(len(split_list), list_item_length(split_list))

    lstrx.len_listr = listr_pre

    lstrx.build_hstrx_len()
    lstrx.build_hstrx_wid()
        

    lstrx.len_slotrix = listrix.slotrix_eater(lstrx)
    lstrx.build_hotrix()

    # game start here-ish
    state_gen()
    failed = False
    while not failed:

        if debug:
            print('hotrix: ')
            print(lstrx.len_hotrix)
            print('slotrix: ')
            print(lstrx.len_slotrix)
            for i in range(26):
                print(chr(i + 97) + ': ' + str(lstrx.letter_chance(i)))

        correct_flag = False
        nnr = ''

        display_state()
        lttr = letter_prompt()
        chance_of_being_right = lstrx.letter_chance(lttr)
        random_value = random.random()

        # IT'S MAGIC, BABY
        if chance_of_being_right > random_value:
            correct_flag = True
            
            print('\nYou guessed right! Press enter to continue.')
            user_input_get()
        else: 
            wrong_guesses += 1
            lstrx.prune_letters(lttr)
            print('\nYou guessed wrong! Press enter to continue.')
            user_input_get()
        if wrong_guesses > max_wrong:
            failed = True
            print('\nBetter luck next time. R to restart, anything else to quit:')
            if user_input_get() == 'r':
                spaceman()
            else: 
                exit

        if correct_flag:
            correct_flag = False
            nnr = hist_choice(lstrx.len_hotrix, lttr)
            lstrx.prune_hotrix(nnr, lttr)
            rebuild_state(nnr, lttr)

            if debug:
                print('nnr: ')
                print(nnr)

        if debug: 
            print('^v^')
            print()
            print(lstrx.removed_word_list)
            print(lstrx.removed_words)

        lstrx.build_hstrx_len()
        lstrx.build_hstrx_wid()
        lstrx.len_slotrix = listrix.slotrix_eater(lstrx)
        lstrx.build_hotrix()

        if letters_complete == game_length:
            restr = ''
            for string in spaceman_state:
                restr = restr + string.replace(' ', '')
            print('\nCongratulations!!! You won!')
            print('The word was "' + restr + '"')
            failed = True
            print('\nR to restart, anything else to quit:')
            if user_input_get() == 'r':
                spaceman()
            else: 
                exit



    # print(lstrx.len_slotrix)
    # print(listrix.slotrix_eater(lstrx))
    # print(lstrx.axial_wid(0,0))
    # print(lstrx.axial_wid(0,0))
    # print(listrix.letter_width_eater(lstrx.axial_wid(0,0))) # Works!
    # print(listrix.word_slot_eater(0, lstrx)) # Also works!
    # print(listrix.slotrix_eater(lstrx)) # Works BEAUTIFUL! 
    '''
    print(lstrx.len_slotrix)
    print(lstrx.len_hotrix)
    print('\n')
    print(hist_choice(lstrx.len_hotrix, 0))
    print('\n')
    for i in range(26):
        print(lstrx.letter_chance(i))
    
    
    '''
    
spaceman()