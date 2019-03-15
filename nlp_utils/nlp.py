
from nltk.corpus import stopwords
from nltk import word_tokenize
import operator

def detect(text):
    text=str(text)
    en=stopwords.words('english')

def treat(name, function):
    final = ""
    tokenized = word_tokenize(name)
    j=0
    test = False
    i=0
    while not test and i<len(tokenized):
        if function in tokenized[i]:
            j=i+1
            test=True
        i+=1
    final = " ".join(tokenized[j:])
    return final