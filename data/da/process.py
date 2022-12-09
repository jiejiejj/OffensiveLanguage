import random,os

base = './'
train = 'train.tsv'
test = 'test.tsv'
label2id = {'NOT\n': '0\n', 'OFF\n': '1\n'}

with open(os.path.join(base, train), 'r', encoding='utf8') as f:
    lines = f.readlines()[1:7001]
    random.shuffle(lines)

write_lines = []
for line in lines:
    try:
        write_lines.append('\t'.join([line.split('\t')[1], label2id[line.split('\t')[2]]]))
    except:
        print(line, line.split('\t'))

with open(os.path.join(base, 'train.txt.final'), 'w', encoding='utf8') as train:
    with open(os.path.join(base, 'dev.txt.final'), 'w', encoding='utf8') as dev:
        index = int(len(write_lines) * 0.9)
        train.write(''.join(write_lines[:index]))
        dev.write(''.join(write_lines[index:]))

with open(os.path.join(base, test), 'r', encoding='utf8') as test:
    with open(os.path.join(base, 'test.txt.final'), 'w', encoding='utf8') as t:
        lines = test.readlines()[1:]
        write_lines = ['\t'.join([line.split('\t')[1], label2id[line.split('\t')[2]]]) for line in lines]
        t.write(''.join(write_lines))