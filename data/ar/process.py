import random,os

base = './'
train = 'train.tsv'
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

id2sent = {}
with open('./offenseval-ar-test-v1.tsv', 'r', encoding='utf8') as f:
    lines = f.readlines()[1:]
    for line in lines:
        id, sent = line.split('\t')
        id2sent[id] = sent.strip()
id2label = {}
with open('./offenseval-ar-labela-v1.csv', 'r', encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        id, label = line.split(',')
        id2label[id] = label2id[label]

with open('./test.txt.final', 'w', encoding='utf8') as f:
    for id, sent in id2sent.items():
        f.write(sent + '\t' + id2label[id])