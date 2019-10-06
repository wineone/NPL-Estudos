# coding: utf8
"""
faz uso da nlpt para procurar sinonimos e significados das palavras
"""
from nltk.corpus import wordnet

syn = wordnet.synsets("pain")

# definições e exemplos
# print syn[0].definition()
# print syn[0].examples()[0]

# print ""


a = wordnet.synsets("NLP")

# print a[0].definition()

# print wordnet.synsets("Python")[1].definition()

# sinonimos

sinonimos = []

for syn in wordnet.synsets("horse"):
    for lemma in syn.lemmas():
        sinonimos.append(lemma.name())

# print sinonimos

# antonimos

antonimos = []

for syn in wordnet.synsets("light"):
    for l in syn.lemmas():
        if l.antonyms():
            for i in l.antonyms():
                antonimos.append(i.name())

print antonimos