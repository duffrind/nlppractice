create map counts, context_counts
counts = dict()
context_counts = dict()

open training_file
    for line in training_file:
        split line into an array of words
        append '</s>' to the end
        prepend '<s>' to the beginning of words
        for each i in 1 to length(words)-1 # Note: starting at 1, after <s>
            counts['wi-1 wi'] += 1
            context_counts['wi-1'] += 1
            counts['wi'] += 1
            context_counts[''] += 1

open model_file for writing
    for each ngram, count in counts
        split ngram into an array of words
        remove the last element of words
        join words into context
        probability = counts[ngram]/context_counts[context]
        print ngram, probability to model_file
