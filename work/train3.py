unigram_prob = dict()
total_count = 0

test = True
train_file = '../data/wiki­-ja-­train.word'
if test:
    train_file = '../test/04­-input.txt'


with open(train_file, 'r') as training_file:
    for line in training_file.read().split('\n')[:-1]:
        for uni in line:
            unigram_prob[uni] = unigram_prob.get(uni, 0) + 1
            total_count += 1

with open('../test/04­-unigram.txt', 'w') as model:
