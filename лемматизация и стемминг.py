from nltk.tokenize import word_tokenize
import nltk
import pandas as pd
from string import punctuation
import pymorphy2


data = pd.read_excel(r'C:\Users\user\Desktop\жопа.xlsx')

string = data['text']

tokens = string[0].split()



from string import punctuation

punctuations = list(punctuation)
punctuations.append('—')

low_tokens = [i.lower() for i in tokens if i not in punctuations]


stopwords = nltk.corpus.stopwords.words('russian')

words_without_stop = [i for i in low_tokens if i not in stopwords]


morph = pymorphy2.MorphAnalyzer()

lemms = [morph.parse(i)[0].normal_form for i in words_without_stop]
print(lemms)