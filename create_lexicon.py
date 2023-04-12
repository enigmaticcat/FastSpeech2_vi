import os
import json

with open('mfa/vietnamese_mfa.dict', 'r', encoding='utf-8') as f:
    with open('lexicon/vietnamese_mfa.txt', 'w', encoding='utf-8') as g:
        # with open('mfa/vietnamese_mfa_fixed.dict', 'w', encoding='utf-8') as h:
        #     words = []
        #     count_dup = 0
        phonemes = []
        for line in f:
            parts = line.split('\t')
            w = parts[0].strip()
                #if w not in words:
            g.write(w + '\t' + parts[5].strip() + '\n') 
            ps = parts[5].strip().split(' ')
            for p in ps:
                if p not in phonemes:
                    phonemes.append(p)
                #     h.write(line.strip() + '\n')
                #     words.append(w)
                # else:
                #     count_dup += 1
        with open('lexicon/vietnamese_mfa_phonemes.json', 'w', encoding='utf-8') as h:
            json.dump(phonemes, h, ensure_ascii=False)
print('Done')