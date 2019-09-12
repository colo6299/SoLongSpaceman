import random
import listrix   # Yeah, I already regret it. kys


# Hey, if I'm going to burn out, better sooner rather than later, right?
# Besides, it's not much of a 'secret' word if the program knows it!

# oh, and Mr/Ms TA,
# I am truly sorry.


guessed_letters = []
spaceman_state = []
wrong_guesses = 0
max_wrong = 15
game_length = 0
letters_complete = 0
s = False


# only works for word slot histogram structure
def hist_choice(hotrix, letter_index):
    """
    Returns a random nnr slot descriptor from the hotrix, for a particular letter index.

    Weighted by the... histogram. Makes sense, yeah?
    """
    return random.choices(hotrix[letter_index][0], hotrix[letter_index][1])


def user_input_get():
    '''
    yeah, it's just input().lower

    I think I accidentally copied it from color checklist? was trying to get mine from madLibs lol
    '''
    # the input function will display a message in the terminal
    # and wait for user input.
    user_in = input()
    return user_in.lower()


def list_item_length(list_in):
    '''
    Returns the length of the longest word in the list.

    Probably.
    '''
    max_len = 0
    for word in list_in:
        if len(word) > max_len:
            max_len = len(word)
    return max_len


def prune_list(list_in, length):
    """
    Returns a pruned list with only words length letters long.
    """
    retlist = list()
    for word in list_in:
        if len(word) == length:
            retlist.append(word)
    return retlist


def decode_nnr(nnr_selection: str):
    """
    Gets rid of those pesky -'s
    """

    return nnr_selection.split('-')


def decode_letter(letter_index):
    """
    Eats a letter index (a == 0) and returns the associated char
    """
    return chr(letter_index + 97)


def load_words_list():
    """
    First off, yikes. Gold medal for awful code.

    Asks user for a word length and returns the loaded word list pruned by that length.
    """
    #  '''
    # A function that reads a text file of words and randomly selects one to use as the secret word
    #     from the list.
    # Returns: 
    #        string: The secret word to be used in the spaceman guessing game <--- hahaa... no
    # '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')

    max_length = list_item_length(words_list)

    print('Word length? ')
    user_input = user_input_get()
    user_input.strip()
    
    if not user_input.isnumeric():  # I just learned this was a thing lol
        return load_words_list()
    elif int(user_input) not in range(max_length):
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
    """
    Asks the user for a guess. Appends valid guesses to the guessed_letters.

    Letters are returned as indices (a == 0)
    """
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
    """
    Initializes or resets the spaceman state (the underscore thing)
    """
    global spaceman_state
    spaceman_state = []
    for i in range(game_length):
        spaceman_state.append('_ ')

def display_state():
    """
    Shows the things! 
    Guessed letters and guessed letters, that is.
    """
    restr = ''
    for string in spaceman_state:
        restr = restr + string
    print()
    print(restr)
    print()
    # It's only all on one line because I didn't want to type print() again. Wait...
    print('Guessed letters: ' + str(guessed_letters) + '\nIncorrect guesses remaining: ' + str(max_wrong - wrong_guesses))
    

def rebuild_state(nnr_choice, letter_index):
    """
    Nothing fancy, rebuilds the spaceman underscore thingy
    """
    global spaceman_state
    for slot in decode_nnr(nnr_choice[0]):
        global letters_complete
        letters_complete += 1
        spaceman_state[int(slot)] = decode_letter(letter_index) + ' '


def space_killer(string):
    """
    pew pew

    yeah it just deletes spaces from a string. Crazy stuff.
    """
    string.replace(' ', '')
    return string


# Now, this is where you ask, "Wyatt, how can you have a spaceman program that doesn't choose a word?"
# Well, I'll update the comment text when I figure that one out.
# UPDATE: it... works? I'm not really sure how. 

def sinister_event(listrix_in, letter_in):
    """
    A 'sinister spaceman' event, replaces removed word... things(?) with their backups,
    handles the current guess for the guesses list.
    """
    # Basically, there are two identical copies of all the stuff below, but
    # the backups are only pruned on correct guesses, not incorrect guesses.
    # In other words, the backups represent what the state of the listrix
    # would be if you had letters in slots, but had no incorrect guesses.
    # Simply swapping the new for the old makes the sinister magic hapen.

    listrix_in.removed_words = listrix_in.removed_words_backup
    listrix_in.removed_word_list = listrix_in.removed_word_list_backup
    listrix_in.len_listr = listrix_in.len_listr_backup

    # this bit over here is for handling the content of the spaceman state.
    # yes, this could be solved with separate 'correct' and 'incorrect' letter
    # lists, but that only works when you know whether the guess is correct
    # when you append it to the guess list. Which... we don't.
    new_guessed_letters = list()
    for lttr in guessed_letters:
        for string in spaceman_state:
            if lttr + ' ' == string:
                new_guessed_letters.append(lttr)

    # just a bit of classic letter index => str conversion. I think I wrote
    # something for this, but I honestly don't really remember.
    new_guessed_letters.append(chr(letter_in + 97))
    return new_guessed_letters


def spaceman():
    '''
    Spaceman init and loop. Can be called to start or restart spaceman.
    '''

    global guessed_letters
    global spaceman_state
    global wrong_guesses
    global max_wrong
    global game_length
    global letters_complete
    global s

    guessed_letters = []
    spaceman_state = []
    wrong_guesses = 0
    max_wrong = 7
    game_length = 0
    letters_complete = 0
    s = False


    print('''

    ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢

    Our stranded spaceman has found a rocket to get home with. One problem- 
    It's locked! There's a keypad attatched to both a geiger counter, and 
    the lock on the hatch. The pad takes a code word, but he can't reach! 
    Can you help the spaceman crack Schrodingers;Code and get back home? 

    It's exactly as easy as it seems. Good luck, you're going to need it.

    ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢
    
    
    Press Enter to continue, or type 'debug' to enable dev view.
    Type 's' to have a bad time. (you can enter both!)

    ''')

    debug = False
    sinister = False
    u_in = user_input_get()
    if 'debug' in u_in:
        debug = True
    
    if 's' in u_in:
        s = True

    split_list = load_words_list()

    # it... uh
    # gimme a sec
    listr_pre = listrix.list_eater(split_list)
    lstrx = listrix.Listrix3()

    # makes the tiny listrix not tiny.
    lstrx.explode(len(split_list), list_item_length(split_list))

    # then slot the proto-list in the listrix
    lstrx.len_listr = listr_pre
    lstrx.len_listr_backup = listr_pre

    # then build the 2d histogram listrix(s) WOOO ITS HAPPENING
    lstrx.build_hstrx_len()
    lstrx.build_hstrx_wid()
        
    # same thing, but for the slot listrix and histograms
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

        # oh boy here it comes
        lttr = letter_prompt()
        chance_of_being_right = lstrx.letter_chance(lttr)
        random_value = random.random()

        # IT'S MAGIC, BABY
        if chance_of_being_right > random_value:
            correct_flag = True
            
            # it's a beautiful day outside. Birds are singing, flowers are blooming...
            if s:
                print('<<YOU FEEL LIKE YOU\'RE HAVING A BAD TIME>>')
                guessed_letters = sinister_event(lstrx, lttr)

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

            # grabs a nnr slot descriptor from the thing and use it to disqualify words
            nnr = hist_choice(lstrx.len_hotrix, lttr)
            lstrx.prune_hotrix(nnr, lttr)
            
            # rebuild the fancy underscore thing
            rebuild_state(nnr, lttr)

            if debug:
                print('nnr: ')
                print(nnr)

        if debug:
            print('^v^')
            print()
            print(lstrx.removed_word_list)
            print(lstrx.removed_words)

        # rebuild the... everything. Yeah, yeah... It still runs in <1s ok?
        lstrx.build_hstrx_len()
        lstrx.build_hstrx_wid()
        lstrx.len_slotrix = listrix.slotrix_eater(lstrx)
        lstrx.build_hotrix()

        # Winner, winner?
        if letters_complete == game_length:
            restr = ''

            # harvests the word from spaceman state. This is the first time the program knows the word. 
            for string in spaceman_state:
                restr = restr + string.replace(' ', '')
            print('\nCongratulations!!! You won!')
            print('The word is "' + restr + '"')  # Updated was => is, after all it's not like it knew...
            failed = True
            print('\nR to restart, anything else to quit:')
            if user_input_get() == 'r':
                spaceman()
            else: 
                exit


    # Random garbage? What random garbage? This is the end of the function.

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

# Thanks, Nathan.
if __name__ == "__main__":
    spaceman()
