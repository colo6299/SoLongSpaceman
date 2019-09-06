import random
import listrix   # Yeah, I already regret it.


# Hey, if I'm going to burn out, better sooner rather than later, right?
# Besides, it's not much of a 'secret' word if the program knows it!

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
    user_input = int(user_input_get())

    if int(user_input) not in range(max_length):
        print('Please enter a number between 1 and ' + str(max_length))
        load_words_list()
    else: 
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




# Now, this is where you ask, "Wyatt, how can you have a spaceman program that doesn't choose a word?"
# Well, I'll update the comment text when I figure that one out.

def spaceman():

    print('''

    ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢
    Our stranded spaceman has found a rocket to get home with. One problem- 
    It's locked! There's a keypad attatched to both a geiger counter, and 
    the lock on the hatch. The pad takes a code word, but he can't reach! 
    Can you help the spaceman break Schrodingers;Code and get back home? 

    It's exactly as easy as it seems. Good luck, you're going to need it.
    ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢
    
    
    Press Enter to continue.

    ''')
    input()

    split_list = load_words_list()
    listr_pre = listrix.list_eater(split_list)
    lstrx = listrix.Listrix3()

    lstrx.explode(len(split_list), list_item_length(split_list))

    lstrx.len_listr = listr_pre

    lstrx.build_hstrx_len()
    lstrx.build_hstrx_wid()

    print(split_list)
    print(listrix.Listrix3.rel_chance(lstrx.hstrx_len))

    
spaceman()