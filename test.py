import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()
tokenizer = RegexpTokenizer(r'\w+')


def getbigramfeatures(sentence):
    tokens = tokenizer.tokenize(sentence)
    lemmas = [wordnet_lemmatizer.lemmatize(word) for word in tokens]
    bigrams = nltk.bigrams(lemmas)
    bigrams = [part[0]+' '+part[1] for part in bigrams]
    bigramfeat = lemmas + bigrams
    return bigramfeat

print(getbigramfeatures('my name is sahil and i study computer science at a university'))