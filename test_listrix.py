from listrix import *

# Look, I did my best
# writing tests for this would have required... planning

def test_bool_eater():

    assert bool_eater([True, False, False, True]) == 2


def test_letter_eater():

    assert letter_eater('a') == [True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    assert letter_eater('a', 26, 96) == [True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]


def test_word_eater():

    assert word_eater('az') == [[True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False], [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True]]