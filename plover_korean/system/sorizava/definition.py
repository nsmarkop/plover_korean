"""Stenography definition for Korean based on the 47-key Sorizava layout."""

from typing import Tuple, Dict, List, Optional


# Consonant groups don't internally follow a steno order when constructing words.
KEYS: Tuple[str] = (
    # 초성 - Initial consonant (except ㅢ as an out of place vowel)
    'ㅊ-', 'ㅌ-', 'ㅋ-', 'ㅂ-', 'ㅍ-',
    'ㅅ-', 'ㄷ-', 'ㅈ-', 'ㄱ-', 'ㅋ-',
    'ㅁ-', 'ㄹ-', 'ㄴ-', 'ㅎ-', 'ㅢ-',

    # 중성 - Medial vowel
    'ㅗ-', 'ㅏ-', 'ㅜ-',
    '-ㅡ', '-ㅓ', '-ㅣ',

    # 종성 - Final consonant
    '-ㄲ', '-ㅎ', '-ㅌ', '-ㅊ', '-ㅍ',
    '-ㄱ', '-ㄴ', '-ㄹ', '-ㅅ', '-ㅂ',
    '-ㅆ', '-ㅇ', '-ㅁ', '-ㄷ', '-ㅈ',

    # Numbers
    '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9', '-0',

    # Space key. This isn't actually in any strokes but all spacing is either
    # in the dictionary entries or explicit with the use of a separate key?
    '*'
)

IMPLICIT_HYPHEN_KEYS: Tuple[str] = (
    'ㅢ-',
    'ㅗ-', 'ㅏ-', 'ㅜ-',
    '-ㅡ', '-ㅓ', '-ㅣ'
)

SUFFIX_KEYS: Tuple[str] = ()

# This system has explicit number keys, so there is no need for these.
NUMBER_KEY: str = ''
NUMBERS: Dict[str, str] = {}

# Can be overridden or alternatives can be made in a dictionary.
UNDO_STROKE_STENO: str = ''

ORTHOGRAPHY_RULES: List[Tuple[str, str]] = []
ORTHOGRAPHY_RULES_ALIASES: Dict[str, str] = {}
ORTHOGRAPHY_WORDLIST: Optional[str] = None

# TODO: Figure out how to handle the duplicate ㅋ keys, or if it's even needed.
KEYMAPS: Dict[str, Dict[str, Tuple[str]]] = {
    'Keyboard': {
        'ㅊ-': '1',
        'ㅌ-': '2',
        'ㅋ-': '3',
        'ㅂ-': '4',
        'ㅍ-': '5',

        'ㅅ-': 'q',
        'ㄷ-': 'w',
        'ㅈ-': 'e',
        'ㄱ-': 'r',
        'ㅋ-': 't',

        'ㅁ-': 'a',
        'ㄹ-': 's',
        'ㄴ-': 'd',
        'ㅎ-': 'f',
        'ㅢ-': 'g',

        'ㅗ-': 'x',
        'ㅏ-': 'c',
        'ㅜ-': 'v',


        '-ㅡ': 'n',
        '-ㅓ': 'm',
        '-ㅣ': ',',

        '-ㄲ': '6',
        '-ㅎ': '7',
        '-ㅌ': '8',
        '-ㅊ': '9',
        '-ㅍ': '0',

        '-ㄱ': 'y',
        '-ㄴ': 'u',
        '-ㄹ': 'i',
        '-ㅅ': 'o',
        '-ㅂ': 'p',

        '-ㅆ': 'h',
        '-ㅇ': 'j',
        '-ㅁ': 'k',
        '-ㄷ': 'l',
        '-ㅈ': ';',

        '-1': 'F1',
        '-2': 'F2',
        '-3': 'F3',
        '-4': 'F4',
        '-5': 'F5',
        '-6': 'F6',
        '-7': 'F7',
        '-8': 'F8',
        '-9': 'F9',
        '-0': 'F10',

        '*': 'space',

        'arpeggiate': 'b',
        'no-op': ()
    }
}

DICTIONARIES_ROOT: str = 'asset:plover_korean:system/sorizava/dictionaries'
DEFAULT_DICTIONARIES: List[str] = [
    'ko_sorizava_base.py',
    'ko_sorizava_main.json'
]
