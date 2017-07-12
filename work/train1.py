counts = dict()
total_count = 0
with open('../test/01-train-input.txt', 'r') as training_file:
    for line in training_file.read().split('\n'):
        words = line.split()
        words.append('</s>')
        for word in words:
            counts[word] = counts.get(word, 0) + 1
            total_count += 1
with open('../test/01-model-file.txt', 'w') as model_file:
    for word, count in counts.iteritems():
        probability = float(counts[word])/total_count
        model_file.write(word + '\t' + str(probability) + '\n')
