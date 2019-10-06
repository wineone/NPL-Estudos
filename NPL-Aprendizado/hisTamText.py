import pandas as pd
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib


def tam(text):
    return len(text)

data = pd.read_csv('train.csv')

data['length'] = data['text'].apply(tam)

# print(data)

EAP = data[data['author'] == 'EAP']
HLP = data[data['author'] == 'HPL']
MWS = data[data['author'] == 'MWS']

# print(MWS)

# print(EAP)
bin = 500

# contagem de palavras em cada obra de cada autor

# plt.hist(EAP['length'],bins=bin,alpha=0.6,label="EAP")
# plt.hist(HLP['length'],bins=bin,alpha=0.8,label='HPL')
# plt.hist(MWS['length'],bins=bin,alpha=0.4,label='MWS')


# matplotlib.rcParams['figure.figsize'] = (12.0, 6.0)

# plt.xlim(0,800)
# plt.legend()
# plt.grid()
# plt.show()

eap_tfid_vector = TfidfVectorizer('english')

eap_tfid_vector.fit(EAP['text'])

eap_dic = eap_tfid_vector.vocabulary_.items()



vocab = []
cont = []

for f,s in eap_dic:
    vocab.append(f)
    cont.append(s)

eap_vocab = pd.Series(cont,index = vocab)

eap_vocab = eap_vocab.sort_values(ascending=False)

top_eap_vocab = eap_vocab.head(20)

top_eap_vocab.plot(kind='barh',xlim=(15200,15300))

plt.show()




# print(data)