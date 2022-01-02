import time
import pickle

startTime=time.time()

unigram = {}
bigram = {}
try:
    with open("unigram.pkl","rb") as unigram_file:
        unigram = pickle.load(unigram_file)
    with open("bigram.pkl","rb") as bigram_file:
        bigram = pickle.load(bigram_file)
    # with open("trigram.pkl","rb") as trigram_file:
    #     trigram = pickle.load(trigram_file)
except FileNotFoundError:
    with open('train_v2.txt', 'r', encoding='utf-8') as f:
        for index, line in enumerate(f):
            # if (index > 10000):
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

    with open("unigram.pkl","wb") as unigram_file:
        pickle.dump(unigram,unigram_file)

    with open("bigram.pkl","wb") as bigram_file:
        pickle.dump(bigram,bigram_file)

finishTime = time.time()
print(f"done in {finishTime - startTime} seconds")
print(unigram)