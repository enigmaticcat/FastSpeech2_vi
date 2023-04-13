import os
import re
import json

lexicon_files = ['./lexicon/vi-new-lexicon.txt', './lexicon/librispeech-lexicon.txt']
new_lexicon_file = './lexicon/mixed-en-vi-lexicon.txt'
new_phones_file = './lexicon/mixed-en-vi-phonemes.json'

def read_lexicon(lex_path, lexicon = {}):
    with open(lex_path, 'r', encoding='utf-8') as f:
        for line in f:
            temp = re.split(r"\s+", line.strip("\n"))
            word = temp[0]
            phones = temp[1:]
            if word.lower() not in lexicon:
                lexicon[word.lower()] = phones
    return lexicon

lexicon = {}
phonemes = []

for fname in lexicon_files:
    read_lexicon(fname, lexicon)

# and write a new lexicon file
with open(new_lexicon_file, 'w', encoding='utf-8') as f:
    for k in lexicon:
        f.write('{}\t{}\n'.format(k, ' '.join(lexicon[k])))
        for p in lexicon[k]:
            if p not in phonemes:
                phonemes.append(p)
    with open(new_phones_file, 'w', encoding='utf-8') as g:
        json.dump(phonemes, g, ensure_ascii=False)
