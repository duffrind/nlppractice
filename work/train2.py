counts = dict()
context_counts = dict()

test = False
file_name = '../data/wiki-en-train.word'
if test:
    file_name = '../test/02-train-input.txt'

with open(file_name, 'r') as training_file:
    for line in training_file.read().split('\n')[:-1]:
        words = ['<s>'] + line.split() + ['</s>']
        for i in range(1, len(words)): # Note: starting at 1, after <s>
            counts[words[i - 1] + ' ' + words[i]] = counts.get(words[i - 1] + ' ' + words[i], 0) + 1
            context_counts[words[i - 1]] = context_counts.get(words[i - 1], 0) + 1
            counts[words[i]] = counts.get(words[i], 0) + 1
            context_counts[''] = context_counts.get('', 0) + 1

with open('../test/02-model-file.txt', 'w') as model_file:
    for ngram, count in counts.iteritems():
        words = ngram.split(' ')
        _ = words.pop()
        context = ' '.join(words)
        probability = float(counts[ngram]) / context_counts[context]
        model_file.write(ngram + '\t' + str(probability) + '\n') #to model_file

# Test train-bigram on test/02-train-input.txt
# Train the model on data/wiki-en-train.word
# Calculate entropy on data/wiki-en-test.word (if linear interpolation, test different values of λ2)

# Challenge:
# Use Witten-Bell smoothing (Linear interpolation is easier)
# Create a program that works with any n (not just bigram)
