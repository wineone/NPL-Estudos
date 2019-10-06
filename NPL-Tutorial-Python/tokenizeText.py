"""
programa que quebra um texto em palavras e verifica as mais requentes
"""

import urllib2
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords

response = urllib2.urlopen("http://php.net/")

html = response.read()

soup = BeautifulSoup(html,"html5lib")

text = soup.get_text(strip=True)

tokens = map(lambda a: a.encode("utf8"),text.split())

# freq = nltk.FreqDist(tokens)

# observando mapas de palavras
# for f,s in freq.items():
#     print "palavra:",f,"/ vezes: ",s

# temos certeza que nesse artigo estamos falando de php kkkkkkkkk
# freq.plot(20,cumulative=False)

# temos que remover stop words


conjunto = stopwords.words("english")
limpa = []

for i in tokens:
    if i not in conjunto:
        limpa.append(i)

frequencia = nltk.FreqDist(limpa)

frequencia.plot(20,cumulative=False)