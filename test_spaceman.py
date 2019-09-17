from spaceman import *


def test_decode_nnr():

    assert decode_nnr('1-2-4') == ['1', '2', '4']


def test_decode_letter():

    assert decode_letter(0) == 'a'


def test_prune_list():

    assert prune_list(['door', 'cat', 'dog', 'person', 'me'], 3) == ['cat', 'dog']

