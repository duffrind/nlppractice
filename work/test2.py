from math import log

lmd1 = ???
lmd2 = ???
V = 1000000
W = 0
H = 0

load model into probs
    for each line in test_file
        split line into an array of words
        append '</s>' to the end and '<s>' to the beginning of words
        for each i in 1 to length(words)-1 # Note: starting at 1, after <s>
            P1 = lmd1 probs['wi'] + (1 – lmd1) / V # Smoothed unigram probability
            P2 = lmd2 probs['wi-1 wi'] + (1 – lmd2) * P1 # Smoothed bigram probability
            H += -log2(P2)
            W += 1

print 'entropy = ' + H/W
