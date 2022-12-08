import os
import random


base = ['./de']
files = ['train.txt', 'test.txt', 'dev.txt']
label2id = {'OTHER': '0', 'OFFENSE': '1'}


for b in base:
    with open(os.path.join(b, files[0]), 'r', encoding='utf8') as f:
        lines = f.readlines()
        random.shuffle(lines)

    with open(os.path.join(b, files[0]), 'w', encoding='utf8') as train:
        with open(os.path.join(b, files[2]), 'w', encoding='utf8') as dev:
            index = int(len(lines) * 0.8)
            train.write(''.join(lines[:index]))
            dev.write(''.join(lines[index:]))

    for f in files:
        with open(os.path.join(b, f), 'r', encoding='utf8') as src:
            with open(os.path.join(b, f + '.final'), 'w', encoding='utf8') as tgt:
                lines = src.readlines()
                random.shuffle(lines)
                for line in lines:
                    sep = line.split('\t')
                    tgt.write(sep[0] + '\t' + label2id[sep[1]] + '\n')
