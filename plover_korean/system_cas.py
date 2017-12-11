'''
Stenography model for Korean based on the CAS layout.
'''

# KEYS defines the stenography system. Organized by rows and hands.
# Consonant groups don't internally follow a steno order when constructing words.
KEYS = (
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

# IMPLICIT_HYPHEN_KEYS defines keys that are treated as implicit hyphens.
# These are usually the keys that separate the hands so the resulting
# stroke only includes an actual hyphen if it it skips these keys
# completely while using either both hands or just the right hand.
IMPLICIT_HYPHEN_KEYS = (
    'ㅗ-', 'ㅏ-', 'ㅜ-',
    '-*', '-ㅓ', '-ㅣ'
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
# NOTE: this seems to have changed from -7ㅇ to -ㅂㄴ at some point from what I've heard,
# but the dictionary I have to work from uses -ㅂㄴ for something useful so I can't change
# it until I'm more confident about what the proper stroke should be for both. -7ㅇ is
# delete instead of backspace in the newer references I've seen.
UNDO_STROKE_STENO = '-7ㅇ'

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
KEYMAPS = {
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

        'ㅗ-': 'x',
        'ㅏ-': 'c',
        'ㅜ-': 'v',


        '-*': 'n',
        '-ㅓ': 'm',
        '-ㅣ': ',',

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
        '-ㅁ': ';',

        'arpeggiate': 'space',
        'no-op': ()
    }
}

# DICTIONARIES_ROOT and DEFAULT_DICTIONARIES define the location of
# the dictionaries included to be used with this system by default.
DICTIONARIES_ROOT = 'asset:plover_korean:dictionaries_cas'
DEFAULT_DICTIONARIES = (
    'main.json',
    'user.json'
)
