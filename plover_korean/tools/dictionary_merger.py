'''
Used for merging dictionaries into a single dictionary.
'''

import os
import json
from utilities import (create_plover_dictionary,
                       MODULE_DIR, FOLDER_DICT_FINAL, FOLDER_DICT_PARTIAL,
                       PREFIX_CAS, PREFIX_SORIZAVA)


DICTIONARIES_CAS = [
    PREFIX_CAS + 'syllables.json',
    PREFIX_CAS + 'english_fingerspelling.json',
    PREFIX_CAS + 'symbols.json',
    PREFIX_CAS + 'briefs.json',
    PREFIX_CAS + 'fundamental.json',
    PREFIX_CAS + 'single_keys.json'
]

DICTIONARIES_SORIZAVA = [

]

def merge_dictionaries(dictionaries: list, output_filename: str):
    '''
    Merges the provided dictionaries into one file.
    '''

    output_data = {}
    # Order here matters! The earlier dictionaries will have entries overwritten by
    # the later dictionaries if duplicate entries are found. This is intentional.
    for dictionary in dictionaries:
        input_path = os.path.join(MODULE_DIR, FOLDER_DICT_PARTIAL, dictionary)
        with open(input_path, 'r', encoding='utf8') as data_file:
            data = json.load(data_file)
            output_data = {**output_data, **data}

    output_path = os.path.join(MODULE_DIR, FOLDER_DICT_FINAL, output_filename)
    create_plover_dictionary(output_path, output_data)

if __name__ == '__main__':
    merge_dictionaries(DICTIONARIES_CAS, PREFIX_CAS + 'main.json')
    merge_dictionaries(DICTIONARIES_SORIZAVA, PREFIX_SORIZAVA + 'main.json')
