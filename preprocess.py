import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt_tab')

text = "This is a sample sentence, showing off the stop words filtration."

tokens = nltk.word_tokenize(text)

stopwords = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stopwords]

print(filtered_tokens)
