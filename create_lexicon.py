import os

with open('mfa/vietnamese_mfa.dict', 'r', encoding='utf-8') as f:
    with open('lexicon/vietnamese_mfa.txt', 'w', encoding='utf-8') as g:
        with open('mfa/vietnamese_mfa_fixed.dict', 'w', encoding='utf-8') as h:
            words = []
            count_dup = 0
            for line in f:
                parts = line.split('\t')
                w = parts[0].strip()
                if w not in words:
                    g.write(w + '\t' + parts[5].strip() + '\n') 
                    h.write(line.strip() + '\n')
                    words.append(w)
                else:
                    count_dup += 1
print('Total duplicate words: ', count_dup)