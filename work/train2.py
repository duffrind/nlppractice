counts = dict()
context_counts = dict()
unique_count = dict()

test = True # False
file_name = '../data/wiki-en-train.word'
if test:
    file_name = '../test/02-train-input.txt'

n = 2 # n-gram: change to anything > 0
if n < 1:
    raise ValueError('n is non-positive')


with open(file_name, 'r') as training_file:
    for line in training_file.read().split('\n')[:-1]:
        words = ['<s>'] * (n - 1) + line.split() + ['</s>']
        for i in range(n - 1, len(words)): # Note: starting at 1, after <s>
            ngram = list()
            for j in range(i - (n-1), i + 1):
                ngram.append(words[j])
            unique_count[ngram[0]] = unique_count.get(ngram[0], set())
            unique_count[ngram[0]].add(' '.join(ngram[1:]))
            ngram_joined = ' '.join(ngram)
            counts[ngram_joined] = counts.get(ngram_joined, 0) + 1
            _ = ngram.pop()
            ngram_joined = ' '.join(ngram)
            context_counts[ngram_joined] = context_counts.get(ngram_joined, 0) + 1
            counts[words[i]] = counts.get(words[i], 0) + 1
            context_counts[''] = context_counts.get('', 0) + 1

with open('../test/02-model-file.txt', 'w') as model_file:
    for ngram, count in counts.iteritems():
        words = ngram.split(' ') # split on space is implied, but explicit is better than implicit (?)
        _ = words.pop()
        context = ' '.join(words)
        probability = float(counts[ngram]) / context_counts[context]
        model_file.write(ngram + '\t' + str(probability) + '\n') #to model_file

with open('../test/02-unique-count.txt', 'w') as unique_file:
    for key, values in unique_count.iteritems():
        unique_file.write(key + '\t' + str(len(values)) + '\n')

# Test train-bigram on test/02-train-input.txt
# Train the model on data/wiki-en-train.word
# Calculate entropy on data/wiki-en-test.word (if linear interpolation, test different values of λ2)

# Challenge:
# Use Witten-Bell smoothing (Linear interpolation is easier)
# λw = 1− u(wi−1)
# i−1 u(wi−1)+c(wi−1)
# u(wi−1)= number of unique words after wi-1
# Create a program that works with any n (not just bigram) CHECK
