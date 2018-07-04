'''
Stenography model for Korean based on the 36-key CAS layout.
'''

# Consonant groups don't internally follow a steno order when constructing words.
KEYS: tuple = (
    '1-', '2-', '3-', '4-', '5-',
    # 초성 - Initial consonant
    'ㅎ-', 'ㅁ-', 'ㄱ-', 'ㅈ-', 'ㄴ-',
    'ㄷ-', 'ㅇ-', 'ㅅ-', 'ㅂ-', 'ㄹ-',

    # 중성 - Medial vowel
    'ㅗ-', 'ㅏ-', 'ㅜ-',
    '-*', '-ㅓ', '-ㅣ',

    '-6', '-7', '-8', '-9', '-0',
    # 종성 - Final consonant
    '-ㅎ', '-ㅇ', '-ㄹ', '-ㄱ', '-ㄷ',
    '-ㅂ', '-ㄴ', '-ㅅ', '-ㅈ', '-ㅁ'
)

# These are usually the keys that separate the hands so the resulting
# stroke only includes an actual hyphen if it it skips these keys
# completely while using either both hands or just the right hand.
IMPLICIT_HYPHEN_KEYS: tuple = (
    'ㅗ-', 'ㅏ-', 'ㅜ-',
    '-*', '-ㅓ', '-ㅣ'
)

# Defines singular keys that can add suffixes to existing entries.
# The stroke to suffix translation mapping needs to be defined in a dictionary.
SUFFIX_KEYS: tuple = ()

# Defines the mapping from normal keys into what they should be in
# numbers for the current stroke when NUMBER_KEY is pressed.
# This system has explicit number keys, so there is no need for this concept.
NUMBER_KEY: str = ''
NUMBERS: dict = {}

# Causes the previous stroke to be undone.
# The stroke for undo can be overridden or alternatives can be made in a dictionary.
UNDO_STROKE_STENO: str = '-ㅂㄴ'

# Defines language specific spelling patterns for suffixes
# as a list of Python regex entries for input and output.
ORTHOGRAPHY_RULES: list = []
# Defines other ways a suffix can be written.
ORTHOGRAPHY_RULES_ALIASES: dict = {}
# Defines a file containing... set words that are the result of
# suffixes I guess? Seems to be a shortcut way of not needing to
# actually evaluate the orthography rules if it is not needed.
ORTHOGRAPHY_WORDLIST: str = None

# This system uses more keys than most machines for western stenography
# which by default won't be configured here.
KEYMAPS: dict = {
    # This is mapped how the CAS keyboard arranges the QWERTY layer.
    # For users of normal QWERTY, some keys should be re-mapped.
    'Keyboard': {
        '1-': '1',
        '2-': '2',
        '3-': '3',
        '4-': '4',
        '5-': '5',

        'ㅎ-': 'q',
        'ㅁ-': 'w',
        'ㄱ-': 'e',
        'ㅈ-': 'r',
        'ㄴ-': 't',

        'ㄷ-': 'a',
        'ㅇ-': 's',
        'ㅅ-': 'd',
        'ㅂ-': 'f',
        'ㄹ-': 'g',

        'ㅗ-': 'z',
        'ㅏ-': 'x',
        'ㅜ-': 'c',


        '-*': 'v',
        '-ㅓ': 'k',
        '-ㅣ': 'n',

        '-6': '6',
        '-7': '7',
        '-8': '8',
        '-9': '9',
        '-0': '0',

        '-ㅎ': 'y',
        '-ㅇ': 'u',
        '-ㄹ': 'i',
        '-ㄱ': 'o',
        '-ㄷ': 'p',

        '-ㅂ': 'h',
        '-ㄴ': 'j',
        '-ㅅ': 'k',
        '-ㅈ': 'l',
        '-ㅁ': 'm',

        'arpeggiate': 'space',
        'no-op': ()
    }
}

DICTIONARIES_ROOT: str = 'asset:plover_korean:cas/dictionaries'
DEFAULT_DICTIONARIES: list = [
    'ko_cas_numbers.py',
    'ko_cas_base.py'
]
