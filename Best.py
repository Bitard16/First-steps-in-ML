#import numpy as np # Возможно пригодится
import nltk # Разделение на токены и работа на анализ тона текста
nltk.download('punkt') # Примеры 
import matplotlib.pyplot as plt
#from pylab import *
from collections import Counter

fulltext = input() # ВВод
fulltextup = list(fulltext) # Разбитие на элементы
al = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z',  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'V', 'X', 'Y', 'Z', ',', ':', '.', ' ',]
tokens = nltk.word_tokenize(fulltext.lower()) # Распределение на слова
tokensm = nltk.Text(tokens)
tags = nltk.pos_tag(tokensm)
Meaning = Counter(tags)
#tokensSen = nltk.sent_tokenize(fulltext)
#print(tokens)
#print(fulltextup)
#tagger.evaluate(fulltext)
#training_sents = nltk.corpus.brown.tagged_sents(categories='news')[:training_count]
#unigram_tagger = nltk.UnigramTagger(training_sents)
#unigram_tagger.tag(testing_sents_notags[10])

print(Counter(fulltextup))
print(Counter(tokens))
Elem = (Counter(fulltextup))
Words = (Counter(tokens))
#fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 4))
plt.subplot(1,2,1)
plt.bar(range(len(Elem)), list(Elem.values()), align='center', color = 'orange')
plt.xticks(range(len(Elem)), list(Elem.keys()))
plt.subplot(1,2,2)
plt.bar(range(len(Words)), list(Words.values()), align='center', color = 'green')
plt.xticks(range(len(Words)), list(Words.keys()))
## Размеры графиков
fig = plt.gcf()
fig.set_size_inches(50, 15)
fig.savefig('resultWordandElem.png', dpi=100)
 #kdjnkdbf
plt.subplot(1,2,2)
plt.bar(range(len(Meaning)), list(Meaning.values()), align='center', color = 'red')
plt.xticks(range(len(Meaning)), list(Meaning.keys()))
fig = plt.gcf()
fig.set_size_inches(50, 15)
fig.savefig('resultWordandElemMean.png', dpi=100)
plt.show()
