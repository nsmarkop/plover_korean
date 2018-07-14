"""Core functionality for the Sorizava-based Korean stenography system."""

from typing import Tuple, List

import hgtk

# TODO: from plover_korean.system.sorizava.util import get_stroke_groups


LONGEST_KEY = 1
OPERATOR_ATTACH = '{^}'

INITIAL = {
    'ㄱ': 'ㄱ',
    'ㄲ': 'ㄱㅎ',
    'ㄴ': 'ㄴ',
    'ㄷ': 'ㄷ',
    'ㄸ': 'ㄷㄹ',
    'ㄹ': 'ㄹ',
    'ㅁ': 'ㅁ',
    'ㅂ': 'ㅂ',
    'ㅃ': 'ㅂㄱ',
    'ㅅ': 'ㅅ',
    'ㅆ': 'ㅅㅁ',
    'ㅇ': '',
    'ㅈ': 'ㅈ',
    'ㅉ': 'ㅈㄴ', # TODO: What is this actually? Best guess
    'ㅊ': 'ㅊ',
    'ㅋ': 'ㅋ', # TODO: Which ㅋ? There are two.
    'ㅌ': 'ㅌ',
    'ㅍ': 'ㅍ',
    'ㅎ': 'ㅎ'
}

MEDIAL = {
    'ㅏ': 'ㅏ',
    'ㅐ': 'ㅏㅣ',
    'ㅑ': 'ㅏㅡ',
    'ㅒ': 'ㅏㅡㅓ', # TODO: What is this actually? Best guess
    'ㅓ': 'ㅓ',
    'ㅔ': 'ㅓㅣ',
    'ㅕ': 'ㅡㅓ',
    'ㅖ': 'ㅏㅓㅣ',
    'ㅗ': 'ㅗ',
    'ㅘ': 'ㅗㅏ',
    'ㅙ': 'ㅗㅏㅣ',
    'ㅚ': 'ㅗㅣ',
    'ㅛ': 'ㅗㅡ',
    'ㅜ': 'ㅜ',
    'ㅝ': 'ㅜㅓ',
    'ㅞ': 'ㅜㅓㅣ',
    'ㅟ': 'ㅜㅣ',
    'ㅠ': 'ㅜㅡ',
    'ㅡ': 'ㅡ',
    'ㅢ': 'ㅢ',
    'ㅣ': 'ㅣ'
}

FINAL = {
    '': '',
    'ㄱ': 'ㄱ',
    'ㄲ': 'ㄲ',
    'ㄳ': 'ㄱㅅ',
    'ㄴ': 'ㄴ',
    'ㄵ': 'ㄴㅈ',
    'ㄶ': 'ㅎㄴ',
    'ㄷ': 'ㄷ',
    'ㄹ': 'ㄹ',
    'ㄺ': 'ㄱㄹ',
    'ㄻ': 'ㄹㅁ',
    'ㄼ': 'ㄹㅂ',
    'ㄽ': 'ㄹㅅ',
    'ㄾ': 'ㅌㄹ',
    'ㄿ': 'ㅍㄹ',
    'ㅀ': 'ㅎㄹ',
    'ㅁ': 'ㅁ',
    'ㅂ': 'ㅂ',
    'ㅄ': 'ㅅㅂ',
    'ㅅ': 'ㅅ',
    'ㅆ': 'ㅆ',
    'ㅇ': 'ㅇ',
    'ㅈ': 'ㅈ',
    'ㅊ': 'ㅊ',
    'ㅋ': 'ㅎㄱ', # TODO: What is this? Best guess
    'ㅌ': 'ㅌ',
    'ㅍ': 'ㅍ',
    'ㅎ': 'ㅎ'
}


def lookup(strokes: Tuple[str]) -> str:
    """Gets the text that the provided strokes would output.

    Args:
        strokes: A tuple of strokes to look up text for.

    Returns:
        The text text output for the stroke.

    Raises:
        KeyError: The lookup failed to find any matching text.
    """

    if len(strokes) != LONGEST_KEY:
        raise KeyError()

    raise KeyError()


def reverse_lookup(text: str) -> List[Tuple[str]]:
    """Gets the possible strokes that would result in the provided text.

    Args:
        text: The text to look up strokes for.

    Returns:
        A list of stroke tuples. An empty list will be returned if no possible
        strokes were found.
    """

    return []
