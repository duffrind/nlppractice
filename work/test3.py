# word segmentation algorithm

# load a map of unigram probabilities # From exercise 1, unigram LM


edges = dict()
best_edge = dict()
best_score = dict()

test = True
model_file = '../test/04-ja-model.txt'
test_file = '../data/wiki­ja­test.word' # might be wrong
if test:
    model_file = '../test/04­-model.txt'
    test_file = '../test/04-input.txt'

with open(model_file, 'r') as model:
    for line in model.read().split('\n')[:-1]:
        for unicode(key), value in line.split():
            edges[key] = float(value)

with open(test_file, 'r') as test:
    for line in test.read().split('\n')[:-1]:
        line = unicode(line)
        best_edge[0] = None
        best_score[0] = 0
        for word_end in line[1:]:
            best_score[word_end] = 999999
            for word_start in line[:-1]:
# for each line in the input
#     # Forward step
#     remove newline and convert line with “unicode()”
#     best_edge[0] = NULL
#     best_score[0] = 0
#     for each word_end in [1, 2, ..., length(line)]
#         best_score[word_end] = 1010 # Set to a very large value for each word_begin in [0, 1, ..., word_end – 1]
#         word = line[word_begin:word_end] # Get the substring
#         if word is in unigram or length(word) = 1 # Only known words
#             prob = Puni(word) # Same as exercise 1
#             my_score = best_score[word_begin] + -log( prob )
#             if my_score < best_score[word_end]
#                 best_score[word_end] = my_score
#                 best_edge[word_end] = (word_begin, word_end)
#     # Backward step
#     words = [ ]
#     next_edge = best_edge[ length(best_edge) – 1 ]
#     while next_edge != NULL
#         # Add the substring for this edge to the words
#         word = line[next_edge[0]:next_edge[1] ]
#         encode word with the “encode()” function
#         append word to words
#         next_edge = best_edge[ next_edge[0] ]
#     words.reverse()
#     join words into a string and print
