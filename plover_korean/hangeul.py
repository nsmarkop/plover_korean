'''
Korean script related helper functions or wrappers.
'''

import hgtk


def is_letter(letter: str) -> bool:
    '''
    Checks if the provided string is a single Korean letter.

    :param letter: Letter to check.

    :return: If the string is a Korean letter.
    '''

    return hgtk.checker.is_jamo(letter)

def is_hangeul(word: str) -> bool:
    '''
    Checks if the provided string is in the Korean script.

    :param word: Word to check.

    :return: If the string is in the Korean script.
    '''

    return hgtk.checker.is_hangul(word)

def get_last_syllable(word: str) -> str:
    '''
    Gets the last syllable block of the given word.

    :param word: The word to use.

    :return: The last syllable block of the word.
    '''

    if len(word) >= 1 and is_hangeul(word):
        last_syllable = word[-1]
    else:
        last_syllable = ''

    return last_syllable

def ends_in_vowel(word: str) -> bool:
    '''
    Checks if the given word ends in a vowel.

    :param word: The word to check.

    :return: If the word ends in a vowel.
    '''

    last_syllable = get_last_syllable(word)

    try:
        is_vowel = last_syllable and not hgtk.checker.has_batchim(last_syllable)
    except:
        is_vowel = False

    return is_vowel

def ends_in_consonant(word: str) -> bool:
    '''
    Checks if the given word ends in a consonant.

    :param word: The word to check.

    :return: If the word ends in a consonant.
    '''

    last_syllable = get_last_syllable(word)

    try:
        is_consonant = last_syllable and hgtk.checker.has_batchim(last_syllable)
    except:
        is_consonant = False

    return is_consonant

def is_last_consonant(word: str, letter_to_match: str) -> bool:
    '''
    Checks if the given word ennds in the provided consonant.

    :param word: The word to check.
    :param letter_to_match: The letter to check for as the last consonant.

    :return: If the word ends in the given consonant.
    '''

    last_syllable = get_last_syllable(word)

    try:
        is_match = (last_syllable and
                    is_letter(letter_to_match) and
                    ends_in_consonant(word) and
                    hgtk.letter.decompose(last_syllable)[-1] == letter_to_match)
    except:
        is_match = False

    return is_match
