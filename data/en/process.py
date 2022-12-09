import random,os

base = './'
train = 'olid-training-v1.0.tsv'
label2id = {'NOT': '0\n', 'OFF': '1\n'}

with open(os.path.join(base, train), 'r', encoding='utf8') as f:
    lines = f.readlines()[1:]
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
with open('./testset-levela.tsv', 'r', encoding='utf8') as f:
    lines = f.readlines()[1:]
    for line in lines:
        id, sent = line.split('\t')
        id2sent[id] = sent.strip()
id2label = {}
with open('./labels-levela.csv', 'r', encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        id, label = line.split(',')
        id2label[id] = label2id[label.strip()]

with open('./test.txt.final', 'w', encoding='utf8') as f:
    for id, sent in id2sent.items():
        f.write(sent + '\t' + id2label[id])