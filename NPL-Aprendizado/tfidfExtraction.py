"""
montamos uma matriz de densidades de palavras para todas as palavras do texto em cada linha do nosso documento csv

consultas em O(1)? não sei, mas isso ta consumindo memoria para um caralho
"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv('train.csv')

tfvec = TfidfVectorizer('english')

tfvec.fit(data['text'])
tfvec_matrix = tfvec.transform(data['text'])

array = tfvec_matrix.todense()

dataFra = pd.DataFrame(array)


print(dataFra)