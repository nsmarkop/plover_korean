'''
Used for merging dictionaries into a single dictionary.
'''

import os
import json

MODULE_DIR = 'plover_korean'
FOLDER_PARTIAL = 'dictionaries_partial'
FOLDER_FINAL = 'dictionaries'

PREFIX_CAS = 'kr_cas_'
DICTIONARIES_CAS = [
    PREFIX_CAS + 'syllables.json',
    PREFIX_CAS + 'english_fingerspelling.json',
    PREFIX_CAS + 'symbols.json',
    PREFIX_CAS + 'briefs.json',
    PREFIX_CAS + 'fundamental.json'
]

PREFIX_SORIZAVA = 'kr_sorizava_'
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
        input_path = os.path.join(MODULE_DIR, FOLDER_PARTIAL, dictionary)
        with open(input_path, 'r', encoding='utf8') as data_file:
            data = json.load(data_file)
            output_data = {**output_data, **data}

    output_path = os.path.join(MODULE_DIR, FOLDER_FINAL, output_filename)
    with open(output_path, 'w', encoding='utf8') as output_file:
        json.dump(output_data, output_file,
                  sort_keys=True, indent=4, ensure_ascii=False)

merge_dictionaries(DICTIONARIES_CAS, PREFIX_CAS + 'main.json')
merge_dictionaries(DICTIONARIES_SORIZAVA, PREFIX_SORIZAVA + 'main.json')
