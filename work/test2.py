from numpy import log2

unique_count = dict()
total_count = dict()
probs = dict()
#lmd1 = 0#???
#lmd2 = 0#???
V = 1000000
W = 0
H = 0

with open('../test/02-total-count.txt', 'r') as total_file:
    for line in total_file.read().split('\n')[:-1]:
        key, value = line.split('\t')
        total_count[key] = int(value)

with open('../test/02-unique-count.txt', 'r') as unique_file:
    for line in unique_file.read().split('\n')[:-1]:
        key, value = line.split('\t')
        unique_count[key] = int(value)

with open('../test/02-model-file.txt', 'r') as model_file:
    for line in model_file.read().split('\n')[:-1]:
        key, value = line.split('\t')
        probs[key] = float(value)

with open('../data/wiki-en-test.word', 'r') as test_file:
    for line in test_file.read().split('\n')[:-1]:
        words = [word.lower() for word in line.split()]
        words = ['<s>'] + words + ['</s>'] #append '</s>' to the end and '<s>' to the beginning of words
        for i in range(1, len(words)): # Note: starting at 1, after <s>
            lmd1 = 1 - (unique_count.get(words[i-1], 0)/(unique_count.get(words[i-1], 0) + total_count.get(words[i-1], 0.0001)))
            lmd2 = 1 - (unique_count.get(words[i], 0)/(unique_count.get(words[i], 0) + total_count.get(words[i], 0.0001)))
            P1 = lmd1 * probs.get(words[i], 0) + (1 - lmd1) / V # Smoothed unigram probability
            P2 = lmd2 * probs.get(words[i-1] + ' ' + words[i], 0) + (1 - lmd2) * P1 # Smoothed bigram probability
            #print(P2)
            if P2 != 0:
                H += -log2(P2)
            W += 1

print('entropy = ' + str(H / W))
