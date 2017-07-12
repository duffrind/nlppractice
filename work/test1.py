from math import log

lambda = 0.95 # 1 - lambda = 0.05
V = 1000000
W = 0
H = 0
probabilities = dict()

with open('../test/01-model-file.txt', 'r') as model_file:
    for line in model_file.read().split('\n')[:-1]:
        k, v = line.split('\t')
        probabilities[k] = v

for each line in test_file:
    split line into an array of words
    append “</s>” to the end of words
    for each w in words
        add 1 to W
        set P= λunk / V
        if probabilities[w] exists
            set P += λ1 * probabilities[w]
        else
            add 1 to unk
            add -log(P, 2) to H

print “entropy = ”+H/W
print “coverage = ” + (W-unk)/W
