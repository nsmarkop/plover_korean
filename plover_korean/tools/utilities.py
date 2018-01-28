'''
Collection of functionality used by different tools.
'''

import json


MODULE_DIR = 'plover_korean'
FOLDER_DICT_FINAL = 'dictionaries'
FOLDER_DICT_PARTIAL = 'dictionaries_partial'

PREFIX_CAS = 'ko_cas_'
PREFIX_SORIZAVA = 'ko_sorizava_'

def create_plover_dictionary(filepath: str, data: dict):
    '''
    Creates a dictionary file from the provided data to be used with Plover.
    '''

    # ensure_ascii=False to make the file output human readable,
    # but have to make sure that the file is utf-8!
    with open(filepath, 'w', encoding='utf-8') as dictionary_file:
        json.dump(data, dictionary_file,
                  sort_keys=True, indent=4, ensure_ascii=False)
