# For reading input files in CSV format
import csv

import string

import nltk

# LOAD AND CLEAN DATA
batch = list()

c1 = 0
c2 = 0
c3 = 0
c4 = 0

def indexesFromSentence(lang, sentence):
    return [word2index[word] for word in sentence.split(' ')]

def tensorFromSentence(lang, sentence):
    indexes = indexesFromSentence(lang, sentence)
    indexes.append(EOS_token)
    return torch.tensor(indexes, dtype=torch.long, device=device).view(-1, 1)

with open('depression_out.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for row in reader:
        if c1 == 12:
            break;
        s = list()
        s.append(row[0])
        s.append(1)
        batch.append(s)
        c1 = c1 + 1

with open('anger_out.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for row in reader:
        if c2 == 4:
            break;
        s = list()
        s.append(row[0])
        s.append(0)
        batch.append(s)
        c2 = c2 + 1

with open('frustration_out.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for row in reader:
        if c3 == 4:
            break;
        s = list()
        s.append(row[0])
        s.append(0)
        batch.append(s)
        c3 = c3 + 1

with open('sad_out.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for row in reader:
        if c4 == 4:
            break;
        s = list()
        s.append(row[0])
        s.append(0)
        batch.append(s)
        c4 = c4 + 1

print(batch)

tknzr = nltk.TweetTokenizer()

word_to_ix = {}
word_to_ix['<sos>'] = 0
word_to_ix['<eos>'] = 1
for sent in batch:
    #print(sent[0])
    #l = sent[0].split()
    #print(l)
    l = tknzr.tokenize(sent[0])
    #print(l)
    for word in l:
        #print(word)
        if word not in word_to_ix:
            word_to_ix[word] = len(word_to_ix)
print(word_to_ix)
