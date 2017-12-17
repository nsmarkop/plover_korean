'''.
Used for merging dictionaries into a single dictionary.
'''

import os
import json

MODULE_DIR = 'plover_korean'
FOLDER_CAS = 'dictionaries_cas'
# Order here matters! The earlier dictionaries will have entries overwritten by
# the later dictionaries if duplicate entries are found. This is intentional.
DICTIONARIES_CAS = [
    'syllables.json',
    'english_fingerspelling.json',
    'symbols.json',
    'briefs.json',
    'fundamental.json'
]

def merge_cas(output_filename: str = 'main.json'):
    '''
    Merges the dictionaries for the CAS layout system into the provided file.
    '''

    output_data = {}
    for dictionary in DICTIONARIES_CAS:
        input_path = os.path.join(MODULE_DIR, FOLDER_CAS, dictionary)
        with open(input_path, 'r', encoding='utf8') as data_file:
            data = json.load(data_file)
            output_data = {**output_data, **data}

    output_path = os.path.join(MODULE_DIR, FOLDER_CAS, output_filename)
    with open(output_path, 'w', encoding='utf8') as output_file:
        json.dump(output_data, output_file,
                  sort_keys=True, indent=4, ensure_ascii=False)

merge_cas()
