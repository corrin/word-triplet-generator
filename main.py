import time

startTime=time.time()

unigram = {}
bigram = {}
with open('train_v2.txt', 'r', encoding='utf-8') as f:
    for index, line in enumerate(f):
        # if(index>10000):
        #     break
        words = line.strip().split(" ")
        for wi, word in enumerate(words):
            word = word.lower()
            try:
                unigram[word] += 1
            except KeyError:
                unigram[word] = 1
            try:
                wordTuple = (words[wi].lower(), words[wi + 1].lower())
            except IndexError:
                pass
            try:
                bigram[wordTuple] += 1
            except KeyError:
                bigram[wordTuple] = 1
finishTime = time.time()
print(f"done in {finishTime - startTime} seconds")