import pandas as pd
import string
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import matplotlib
from matplotlib import pyplot as plt
from nltk.stem.snowball import SnowballStemmer

sw = stopwords.words('english')
# sw = np.array(sw)

data = pd.read_csv("train.csv")

stemmer = SnowballStemmer('english')

# print data
def removePunc(text):
    trans = str.maketrans('','',string.punctuation)
    return text.translate(trans)

def removeStop(text):
    global sw
    lis = text.split()
    lis = [pal for pal in lis if pal not in sw and not pal.isdigit()]
    return " ".join(lis)

def stemText(text):
    global stemmer
    text = [stemmer.stem(pal) for pal in text.split()]
    return " ".join(text)

data['text'] = data['text'].apply(removePunc)
data['text'] = data['text'].apply(removeStop)
data['text'] = data['text'].apply(stemText)

# print(data.head(10))

tfidVec = TfidfVectorizer('english')

tfidVec.fit(data['text'])

dic = tfidVec.vocabulary_.items()

vocab = []
cont = []

for f,s in dic:
    vocab.append(f)
    cont.append(s)

vocabStem = pd.Series(cont,index = vocab)

vocabStem = vocabStem.sort_values(ascending=False)

# vocabSemStem.plot()

topVocab = vocabStem.head(20)

#  print(topVocab)

# print topVocab
# pd.plotting.register_matplotlib_converters()

topVocab.plot(kind = 'barh',xlim=(15200,15240))

plt.show()

# topVocab.show()