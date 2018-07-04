'''
Core functionality for the CAS-based Korean stenography system.
'''

from typing import Tuple, List

import hgtk
from plover.steno import normalize_stroke
from plover.formatting import META_ATTACH_FLAG, META_START, META_END
from plover_korean.cas.util import get_stroke_groups


# No support for multi-stroke lookups in this dictionary
LONGEST_KEY = 1
OPERATOR_ATTACH = f'{META_START}{META_ATTACH_FLAG}{META_END}'

# TODO: Consider adding a combo INITIAL / MEDIAL list for
#       conjunction cases like 그리 = ㄱㄹㅣ and 그러 = ㄱㄹㅓ
#       to make words like 그런, 그릴, etc.
INITIAL = {
    # Base functionality
    'ㄱ': 'ㄱ',
    'ㄱㅇ': 'ㄲ',
    'ㄴ': 'ㄴ',
    'ㄷ': 'ㄷ',
    'ㄷㅇ': 'ㄸ',
    'ㄹ': 'ㄹ',
    'ㅁ': 'ㅁ',
    'ㅂ': 'ㅂ',
    'ㅇㅂ': 'ㅃ',
    'ㅅ': 'ㅅ',
    'ㅇㅅ': 'ㅆ',
    '': 'ㅇ',
    'ㅈ': 'ㅈ',
    'ㅈㅇ': 'ㅉ',
    'ㅎㅈ': 'ㅊ',
    'ㅎㄱ': 'ㅋ',
    'ㅎㄷ': 'ㅌ',
    'ㅎㅂ': 'ㅍ',
    'ㅎ': 'ㅎ'

    # Special cases

    # Add additional user cases here
}

MEDIAL = {
    # Base functionality
    'ㅏ': 'ㅏ',
    'ㅏㅣ': 'ㅐ',
    'ㅏ*': 'ㅑ',
    'ㅏ*ㅓ': 'ㅒ',
    'ㅓ': 'ㅓ',
    'ㅓㅣ': 'ㅔ',
    '*ㅓ': 'ㅕ',
    'ㅗㅓㅣ': 'ㅖ',
    'ㅗ': 'ㅗ',
    'ㅗㅏ': 'ㅘ',
    'ㅗㅏㅣ': 'ㅙ',
    'ㅗㅣ': 'ㅚ',
    'ㅗ*': 'ㅛ',
    'ㅜ': 'ㅜ',
    'ㅜㅓ': 'ㅝ',
    'ㅜㅓㅣ': 'ㅞ',
    'ㅜㅣ': 'ㅟ',
    'ㅜ*': 'ㅠ',
    'ㅏㅓ': 'ㅡ',
    'ㅏㅓㅣ': 'ㅢ',
    'ㅣ': 'ㅣ'

    # Special cases

    # Add additional user cases here
}

FINAL = {
    # Base functionality
    '': '',
    'ㄱ': 'ㄱ',
    'ㅇㄱ': 'ㄲ',
    'ㄱㅅ': 'ㄳ',
    'ㄴ': 'ㄴ',
    'ㄴㅈ': 'ㄵ',
    'ㅎㄴ': 'ㄶ',
    'ㄷ': 'ㄷ',
    'ㄹ': 'ㄹ',
    'ㄹㄱ': 'ㄺ',
    'ㄹㅁ': 'ㄻ',
    'ㄹㅂ': 'ㄼ',
    'ㄹㅅ': 'ㄽ',
    'ㅎㄹㄷ': 'ㄾ',
    'ㅎㄹㅂ': 'ㄿ',
    'ㅎㄹ': 'ㅀ',
    'ㅁ': 'ㅁ',
    'ㅂ': 'ㅂ',
    'ㅂㅅ': 'ㅄ',
    'ㅅ': 'ㅅ',
    'ㅇㅅ': 'ㅆ',
    'ㅇ': 'ㅇ',
    'ㅈ': 'ㅈ',
    'ㅎㅈ': 'ㅊ',
    'ㅎㄱ': 'ㅋ',
    'ㅎㄷ': 'ㅌ',
    'ㅎㅂ': 'ㅍ',
    'ㅎ': 'ㅎ',

    # Conjugations
    'ㄷㄴ': 'ㄴ다',
    'ㅂㄴ': 'ㅂ니다',
    'ㅂㄴㅅㅈ': 'ㅆ습니다',
    'ㄷㅅ': 'ㅆ다',
    'ㅂㄴㅅ': 'ㅂ니까',
    'ㅂㄴㅅㅁ': 'ㅆ습니까',
    'ㄷㅂㅅ': 'ㅂ시다',
    'ㅇㄴ': '운',
    'ㅇㄹ': '울',
    'ㅇㅁ': '움',
    'ㄱㄴ': 'ㄴ가',
    'ㄷㄴ': 'ㄴ다',
    'ㄱㄷㄴ': 'ㄴ다고',
    'ㄱㄴㅈ': 'ㄴ지',
    'ㄴㅈ': 'ㄴ지',
    'ㄹㄷ': 'ㄹ 때',
    'ㄹㅅ': 'ㄹ 수',
    'ㄹㅈ': 'ㄹ지',
    'ㄹㄱㅁ': 'ㄹ까',
    'ㄹㄱ': 'ㄹ까',
    'ㄷㅂ': 'ㅂ다',
    'ㄱㅂ': 'ㅂ게',
    'ㅂㅅㅈ': 'ㅂ고',
    'ㅂㅈ': 'ㅂ지',
    'ㅂㅈㅁ': 'ㅂ지만',

    # Particles
    # TODO: should they all have automatic spaces
    'ㄱㄷ': '가',
    'ㅅㅈ': '게',
    'ㅇㄹㄱㄷ': '고',
    'ㄷㅈ': '다',
    'ㄴㅅㅈㅁ': '는',
    'ㅎㅇㄹ': '라',
    'ㅇㄹㄱ': '어',
    'ㄹㄴㅅ': '나',
    'ㄴㅅ': '니',
    'ㄴㅅㅈ': '니까',
    'ㄴㅁ': '면',
    'ㄴㅅㅁ': '면서',
    'ㄷㅁ': '도',
    'ㄹㄱㄷ': '도록',
    'ㄱㅈ': '지',
    'ㅈㅁ': '지만',
    'ㅎㄷㅂ': '부터'

    # Special cases

    # Add additional user cases here
}

def lookup(strokes: Tuple[str]) -> str:
    '''
    Get the translation that the provided strokes would output.

    :param strokes: A tuple of strokes to look up translations for.
    :return: The translation. A KeyError will be thrown if the lookup fails.
    '''

    if len(strokes) != LONGEST_KEY:
        raise KeyError()
    initial, medial, final, numbers = get_stroke_groups(strokes[0])

    if numbers:
        raise KeyError()

    # Compose the output
    try:
        text = f'{INITIAL[initial]}{MEDIAL[medial]}{FINAL[final]}'
        output = hgtk.text.compose(f'{text}{hgtk.text.DEFAULT_COMPOSE_CODE}')
    except Exception:
        raise KeyError()

    return f'{output}{OPERATOR_ATTACH}'

def reverse_lookup(text: str) -> List[Tuple[str]]:
    '''
    Get the strokes that would result in the provided text.

    :param text: The text to look up strokes for.
    :return: A list of stroke tuples. Empty list if nothing was found.
    '''

    output = []

    return output
    # TODO: Don't proceed further yet, still in progress.
    #       1ㅎ-ㅇ crashes the suggestions window

    # TODO: I get stroke delimiters in between each letter. Why?
    # Currently, can only look up single syllable block cases
    try:
        initial, medial, final = hgtk.letter.decompose(text)
        stroke = []

        for key, value in INITIAL.items():
            if value == initial:
                for letter in key:
                    stroke.append(f'{letter}-')
                break

        for key, value in MEDIAL.items():
            if value == medial:
                for letter in key:
                    if letter in ['ㅗ', 'ㅏ', 'ㅜ']:
                        stroke.append(f'{letter}-')
                    else:
                        stroke.append(f'-{letter}')
                break

        for key, value in FINAL.items():
            if value == final:
                for letter in key:
                    stroke.append(f'-{letter}')
                break

        output.append(normalize_stroke(stroke))
    except:
        output = []

    return output
