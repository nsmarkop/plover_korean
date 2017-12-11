'''
Stenography model for Korean based on the Sorizava / 소리자바 layout.
'''

# KEYS defines the stenography system. Organized by rows and hands.
# Consonant groups don't internally follow a steno order when constructing words.
KEYS = (
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

    # Space key - this isn't actually in any strokes but it's needed for this system
    # as all spacing is either defined in the dictionary entries or explicit.
    'SPACE'
)

# IMPLICIT_HYPHEN_KEYS defines keys that are treated as implicit hyphens.
# These are usually the keys that separate the hands so the resulting
# stroke only includes an actual hyphen if it it skips these keys
# completely while using either both hands or just the right hand.
IMPLICIT_HYPHEN_KEYS = (
    'ㅢ-',
    'ㅗ-', 'ㅏ-', 'ㅜ-',
    '-ㅡ', '-ㅓ', '-ㅣ'
)

# SUFFIX_KEYS defines singular keys that can add suffixes to existing entries.
# The version with the suffix needs to be defined in a dictionary.
SUFFIX_KEYS = ()

# NUMBERS is used to define the mapping from normal keys into what they
# should be in numbers for the current stroke when NUMBER_KEY is pressed.
# This system has explicit number keys, so there is no need for this concept.
NUMBER_KEY = ''
NUMBERS = {}

# UNDO_STROKE_STENO is what input causes the previous stroke to be undone.
# The stroke for undo can be overridden or alternatives can be made in a dictionary.
UNDO_STROKE_STENO = ''

# ORTHOGRAPHY_RULES defines language specific spelling patterns for
# suffixes as an array of Python regex entries for input and output.
ORTHOGRAPHY_RULES = []
# ORTHOGRAPHY_RULES_ALIASES defines other ways a suffix can be written.
ORTHOGRAPHY_RULES_ALIASES = {}
# ORTHOGRAPHY_WORDLIST defines a file containing... set words that are the
# result of suffixes I guess? Seems to be a shortcut way of not needing to
# actually evaluate the the orthography rules if it is not needed.
ORTHOGRAPHY_WORDLIST = None

# KEYMAPS defines the default mappings used for the various different
# supported machines. This system uses more keys than most machines
# for western stenography which by default won't be configured here.
# It also has more keys than a normal keyboard, but some default layout
# needs to exist. You can rebind to not have a number row if needed.
KEYMAPS = {
    'Keyboard': {
        'ㅊ-': 'q',
        'ㅌ-': 'w',
        'ㅋ-': 'e',
        'ㅂ-': 'r',
        'ㅍ-': 't',

        'ㅅ-': 'a',
        'ㄷ-': 's',
        'ㅈ-': 'd',
        'ㄱ-': 'f',
        'ㅋ-': 'g',

        'ㅁ-': 'z',
        'ㄹ-': 'x',
        'ㄴ-': 'c',
        'ㅎ-': 'v',
        'ㅢ-': 'b',

        # No reasonable defaults for the vowel keys on a standard keyboard.
        # This system requires something like an Ergodox in practice.
        'ㅗ-': '',
        'ㅏ-': '',
        'ㅜ-': '',


        '-ㅡ': '',
        '-ㅓ': '',
        '-ㅣ': '',

        '-ㄲ': 'y',
        '-ㅎ': 'u',
        '-ㅌ': 'i',
        '-ㅊ': 'o',
        '-ㅍ': 'p',

        '-ㄱ': 'h',
        '-ㄴ': 'j',
        '-ㄹ': 'k',
        '-ㅅ': 'l',
        '-ㅂ': ';',

        '-ㅆ': 'n',
        '-ㅇ': 'm',
        '-ㅁ': ',',
        '-ㄷ': '.',
        '-ㅈ': '/',

        '-1': '1',
        '-2': '2',
        '-3': '3',
        '-4': '4',
        '-5': '5',
        '-6': '6',
        '-7': '7',
        '-8': '8',
        '-9': '9',
        '-0': '0',

        'SPACE': 'space',

        'arpeggiate': '',
        'no-op': ()
    }
}

# DICTIONARIES_ROOT and DEFAULT_DICTIONARIES define the location of
# the dictionaries included to be used with this system by default.
DICTIONARIES_ROOT = 'asset:plover_korean:dictionaries_sorizava'
DEFAULT_DICTIONARIES = (
    'main.json',
    'user.json'
)
