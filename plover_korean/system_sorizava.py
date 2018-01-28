'''
Stenography model for Korean based on the 47-key Sorizava layout.
'''

# TODO: Figure out how to handle the duplicate ㅋ keys, or if it's even needed.

# KEYS defines the stenography system. Organized by rows and hands.
# Consonant groups don't internally follow a steno order when constructing words.
KEYS: tuple = (
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

    # Space key - this isn't actually in any strokes but all spacing is either
    # defined in the dictionary entries or explicit with the use of a separate key.
    'SPACE'
)

# IMPLICIT_HYPHEN_KEYS defines keys that are treated as implicit hyphens.
# These are usually the keys that separate the hands so the resulting
# stroke only includes an actual hyphen if it it skips these keys
# completely while using either both hands or just the right hand.
IMPLICIT_HYPHEN_KEYS: tuple = (
    'ㅢ-',
    'ㅗ-', 'ㅏ-', 'ㅜ-',
    '-ㅡ', '-ㅓ', '-ㅣ'
)

# SUFFIX_KEYS defines singular keys that can add suffixes to existing entries.
# The version with the suffix needs to be defined in a dictionary.
SUFFIX_KEYS: tuple = ()

# NUMBERS is used to define the mapping from normal keys into what they
# should be in numbers for the current stroke when NUMBER_KEY is pressed.
# This system has explicit number keys, so there is no need for this concept.
NUMBER_KEY: str = ''
NUMBERS: dict = {}

# UNDO_STROKE_STENO is what input causes the previous stroke to be undone.
# The stroke for undo can be overridden or alternatives can be made in a dictionary.
UNDO_STROKE_STENO: str = ''

# ORTHOGRAPHY_RULES defines language specific spelling patterns for
# suffixes as a list of Python regex entries for input and output.
ORTHOGRAPHY_RULES: list = []
# ORTHOGRAPHY_RULES_ALIASES defines other ways a suffix can be written.
ORTHOGRAPHY_RULES_ALIASES: dict = {}
# ORTHOGRAPHY_WORDLIST defines a file containing... set words that are the
# result of suffixes I guess? Seems to be a shortcut way of not needing to
# actually evaluate the the orthography rules if it is not needed.
ORTHOGRAPHY_WORDLIST: str = None

# KEYMAPS defines the default mappings used for the various different
# supported machines. This system uses more keys than most machines
# for western stenography which by default won't be configured here.
KEYMAPS: dict = {
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

        'SPACE': 'space',

        'arpeggiate': 'b',
        'no-op': ()
    }
}

# DICTIONARIES_ROOT and DEFAULT_DICTIONARIES define the location of
# the dictionaries included to be used with this system by default.
# The dictionaries listed earlier have priority when used.
DICTIONARIES_ROOT: str = 'asset:plover_korean:dictionaries'
DEFAULT_DICTIONARIES: list = [
    'ko_sorizava_main.json'
]
