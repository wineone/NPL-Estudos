# coding: utf8
"""
tenta fazer a mesma coisa que o primeiro mas com auxilio 
da nlpt
"""
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

text = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."

token = sent_tokenize(text)
word = word_tokenize(text)

# print token
# print word

# portugues agora

text = "Ola Mr. Adam, como vai voce? Eu espero que esteja tudo bem. Hoje e um otimo dia, vejo voce depois."

token = sent_tokenize(text,"portuguese")

print token