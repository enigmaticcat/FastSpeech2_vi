import os

with open('mfa/vietnamese_mfa.dict', 'r', encoding='utf-8') as f:
    with open('lexicon/vietnamese_mfa.txt', 'w', encoding='utf-8') as g:
        for line in f:
            parts = line.split('\t')
            g.write(parts[0].strip() + '\t' + parts[5].strip() + '\n') 