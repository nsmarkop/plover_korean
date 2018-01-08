'''
Generator for all syllable block combinations.
'''

import os
import hgtk
from plover_korean.tools.utilities import (create_plover_dictionary,
                                           MODULE_DIR, FOLDER_DICT_PARTIAL,
                                           PREFIX_CAS, PREFIX_SORIZAVA)


SYLLABLE_DICT_FILENAME = 'syllables.json'
ATTACH = '{^}'

STROKES_CAS = {
    'initial': {
        'ㄱ': 'ㄱ',
        'ㄲ': 'ㄱㅇ',
        'ㄴ': 'ㄴ',
        'ㄷ': 'ㄷ',
        'ㄸ': 'ㄷㅇ',
        'ㄹ': 'ㄹ',
        'ㅁ': 'ㅁ',
        'ㅂ': 'ㅂ',
        'ㅃ': 'ㅇㅂ',
        'ㅅ': 'ㅅ',
        'ㅆ': 'ㅇㅅ',
        'ㅇ': '',
        'ㅈ': 'ㅈ',
        'ㅉ': 'ㅈㅇ',
        'ㅊ': 'ㅎㅈ',
        'ㅋ': 'ㅎㄱ',
        'ㅌ': 'ㅎㄷ',
        'ㅍ': 'ㅎㅂ',
        'ㅎ': 'ㅎ'
    },

    'medial': {
        'ㅏ': 'ㅏ',
        'ㅐ': 'ㅏㅣ',
        'ㅑ': 'ㅏ*',
        'ㅒ': 'ㅏ*ㅓ',
        'ㅓ': 'ㅓ',
        'ㅔ': 'ㅓㅣ',
        'ㅕ': '*ㅓ',
        'ㅖ': 'ㅗㅓㅣ',
        'ㅗ': 'ㅗ',
        'ㅘ': 'ㅗㅏ',
        'ㅙ': 'ㅗㅏㅣ',
        'ㅚ': 'ㅗㅣ',
        'ㅛ': 'ㅗ*',
        'ㅜ': 'ㅜ',
        'ㅝ': 'ㅜㅓ',
        'ㅞ': 'ㅜㅓㅣ',
        'ㅟ': 'ㅜㅣ',
        'ㅠ': 'ㅜ*',
        'ㅡ': 'ㅏㅓ',
        'ㅢ': 'ㅏㅓㅣ',
        'ㅣ': 'ㅣ'
    },

    'final': {
        '': '',
        'ㄱ': 'ㄱ',
        'ㄲ': 'ㅇㄱ',
        'ㄳ': 'ㄱㅅ',
        'ㄴ': 'ㄴ',
        'ㄵ': 'ㄴㅈ',
        'ㄶ': 'ㅎㄴ',
        'ㄷ': 'ㄷ',
        'ㄹ': 'ㄹ',
        'ㄺ': 'ㄹㄱ',
        'ㄻ': 'ㄹㅁ',
        'ㄼ': 'ㄹㅂ',
        'ㄽ': 'ㄹㅅ',
        'ㄾ': 'ㅎㄹㄷ',
        'ㄿ': 'ㅎㄹㅂ',
        'ㅀ': 'ㅎㄹ',
        'ㅁ': 'ㅁ',
        'ㅂ': 'ㅂ',
        'ㅄ': 'ㅂㅅ',
        'ㅅ': 'ㅅ',
        'ㅆ': 'ㅇㅅ',
        'ㅇ': 'ㅇ',
        'ㅈ': 'ㅈ',
        'ㅊ': 'ㅎㅈ',
        'ㅋ': 'ㅎㄱ',
        'ㅌ': 'ㅎㄷ',
        'ㅍ': 'ㅎㅂ',
        'ㅎ': 'ㅎ'
    }
}

STROKES_SORIZAVA = {
    'initial': {
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
        'ㅉ': 'ㅈㄴ', # TODO: what is this? best guess following other patterns
        'ㅊ': 'ㅊ',
        'ㅋ': 'ㅋ', # TODO: which ㅋ?
        'ㅌ': 'ㅌ',
        'ㅍ': 'ㅍ',
        'ㅎ': 'ㅎ'
    },

    'medial': {
        'ㅏ': 'ㅏ',
        'ㅐ': 'ㅏㅣ',
        'ㅑ': 'ㅏㅡ',
        'ㅒ': 'ㅏㅡㅓ', # TODO: what is this?
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
    },

    'final': {
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
        'ㅋ': 'ㅎㄱ', # TODO: what is this?
        'ㅌ': 'ㅌ',
        'ㅍ': 'ㅍ',
        'ㅎ': 'ㅎ'
    }
}

def generate_syllable_blocks(stroke_definitions: dict, filename: str):
    '''
    Generates a dictionary for all possible syllable blocks according to
    the provided definitions.
    '''

    data = {}
    for key_initial, value_inital in stroke_definitions['initial'].items():
        for key_medial, value_medial in stroke_definitions['medial'].items():
            for key_final, value_final in stroke_definitions['final'].items():
                stroke = value_inital + value_medial + value_final
                # Attach on both sides for now to work around Plover's automatic spacing
                output = ATTACH + hgtk.letter.compose(key_initial, key_medial, key_final) + ATTACH

                data[stroke] = output

    create_plover_dictionary(os.path.join(MODULE_DIR, FOLDER_DICT_PARTIAL, filename), data)

if __name__ == '__main__':
    generate_syllable_blocks(STROKES_CAS, PREFIX_CAS + SYLLABLE_DICT_FILENAME)
    # generate_syllable_blocks(STROKES_SORIZAVA, PREFIX_SORIZAVA + SYLLABLE_DICT_FILENAME)
