'''
Reusable functionality needed throughout the system.
'''

from typing import Tuple, Callable
import re


STROKE_REGEX = re.compile(r'''
    ^
    (?P<number_start> [12345]*)
    (?P<initial> [ㅎㅁㄱㅈㄴㄷㅇㅅㅂㄹ]*)
    (?P<medial> [ㅗㅏㅜ\-*ㅓㅣ]*)
    (?P<number_end> [67890]*)
    (?P<final> [ㅎㅇㄹㄱㄷㅂㄴㅅㅈㅁ]*)
    $
    ''', re.VERBOSE)

STENO_DASH = '-'

def get_stroke_groups(stroke: str) -> Tuple[str, str, str, str]:
    '''
    Parse a stroke into its logical stroke groups.

    :param stroke: The stroke to create groups from.

    :return: A tuple of the following, all in steno order:
             The keys in the "initial" group of the stroke.
             The keys in the "medial" group of the stroke.
             The keys in the "final" group of the stroke.
             The keys in the "number" group of the stroke.
    :raises: KeyError
    '''

    # Process the stroke into logical groups for processing
    result = STROKE_REGEX.match(stroke)
    if not result:
        raise KeyError()

    stroke_groups = result.groupdict()
    initial = stroke_groups.get('initial')
    medial = stroke_groups.get('medial')
    final = stroke_groups.get('final', '')
    numbers = (stroke_groups.get('number_start', '')
               + stroke_groups.get('number_end', ''))

    # Pull out the dash from the medial if it exists as it causes
    # problems if caller assumes only valid "keys" are in the string
    medial = medial.replace(STENO_DASH, '')

    return initial, medial, final, numbers

def compare_numeric_text(text: str, relate: Callable) -> bool:
    '''
    Checks each sequential entry in a numeric string for a relationship.

    :param text: The string to check.
    :param relate: The operator function to compare sequential entries with.

    :return: If the string sequentially follows the provided relationship.
    '''

    if not text.isdigit():
        return False

    current = text[0]
    for number in text[1:]:
        if relate(number, current):
            current = number
        else:
            return False

    return True
