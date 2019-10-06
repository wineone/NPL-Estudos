from nltk.stem import WordNetLemmatizer

lemma = WordNetLemmatizer()

print lemma.lemmatize("increases",pos="v")