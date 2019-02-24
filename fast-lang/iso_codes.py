# -*- coding: utf-8 -*-
"""Language ISO codes
https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
"""
from os import path
import re

__all__ = [
    'CODES_FILE',
    'iso_codes'
]

# default model location
CODES_FILE = path.join(path.dirname(__file__), 'data', 'lang_iso_codes.csv')

with open(CODES_FILE, 'r') as f:
    data = f.readlines()

iso_codes = dict()
for row in data:
    row = re.sub('\s*', '', row)
    cols = row.split(',')
    iso_codes[cols[1]] = cols[0]

if __name__ == '__main__':
    print(iso_codes)
