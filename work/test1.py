from math import log

lmd = 0.95 # 1 - lmd = 0.05
V = 1000000
W = 0
H = 0
unk = 0
probabilities = dict()

with open('../test/01-model-file.txt', 'r') as model_file:
    for line in model_file.read().split('\n')[:-1]:
        k, v = line.split('\t')
        probabilities[k] = float(v)

with open('../test/01-test-input.txt', 'r') as test_file:
    for line in test_file.read().split('\n')[:-1]:
        words = line.split()
        words.append("</s>")
        for w in words:
            W += 1
            P = (1 - lmd) / V
            if probabilities.get(w, None) != None:
                P += lmd * probabilities[w]
            else:
                unk += 1
            H += -log(P, 2)

print "entropy = " + str(H/W) # currently, H is incorrect
print "coverage = " + str(float(W-unk)/W)
