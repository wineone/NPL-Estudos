"""
montamos uma matriz de densidades de palavras para todas as palavras do texto em cada linha do nosso documento csv

consultas em O(1)? não sei, mas isso ta consumindo memoria para um caralho
"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# imports para treinar os modelos de naive bayes

from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, log_loss
from sklearn.model_selection import GridSearchCV

data = pd.read_csv('train.csv')

tfvec = TfidfVectorizer('english')

tfvec.fit(data['text'])
tfvec_matrix = tfvec.transform(data['text'])

array = tfvec_matrix.todense()

dataFra = pd.DataFrame(array)

dataFra['output'] = data['author']
dataFra['id'] = data['id']

cara = dataFra.columns.tolist()
cara.remove('output')
cara.remove('id')


print(cara)