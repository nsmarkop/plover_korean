KEYS = (
    'ㅎ-', 'ㅁ-', 'ㄱ-', 'ㅈ-', 'ㄴ-',
    'ㄷ-', 'ㅇ-', 'ㅅ-', 'ㅂ-', 'ㄹ-',
    'ㅗ-', 'ㅏ-', 'ㅜ-',

    '-*', '-ㅓ', '-ㅣ',
    '-ㅎ', '-ㅇ', '-ㄹ', '-ㄱ', '-ㄷ',
    '-ㅂ', '-ㄴ', '-ㅅ', '-ㅈ', '-ㅁ'
)

IMPLICIT_HYPHEN_KEYS = ()

SUFFIX_KEYS = ()

NUMBER_KEY = ''

NUMBERS = {}

UNDO_STROKE_STENO = ''

ORTHOGRAPHY_RULES = []
ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = ''

KEYMAPS = {
    'Keyboard': {
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
        'no-op' : ()
    }
}

DICTIONARIES_ROOT = 'asset:plover_korean_cas:dictionaries'
DEFAULT_DICTIONARIES = (
    'main.json',
    'user.json'
)
