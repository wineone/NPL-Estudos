from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer

stemmer = PorterStemmer()

# print stemmer.stem("loneliness")

# stemming palavras em portugues

# print SnowballStemmer.languages

stemmer = SnowballStemmer('portuguese')

print stemmer.stem("lavando")