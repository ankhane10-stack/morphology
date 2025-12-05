import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt_tab')


text = "This is a sample sentence, showing off the stop words filtration."

tokens = nltk.word_tokenize(text)

stopwords = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stopwords]

print(filtered_tokens)

arabic_text = "اكتب حواراً بين شخصين يختلفان في الرأي حول أهمية التكنولوجيا في حياتنا"
arabic_tokens = nltk.tokenize.wordpunct_tokenize(arabic_text)
#arabic_stopwords = stopwords.words('arabic')
#filtered_arabic_tokens = [word for word in arabic_tokens if word not in arabic_stopwords]
#print(filtered_arabic_tokens)
print(arabic_tokens)

arb_stopwords = set(nltk.corpus.stopwords.words('arabic'))
print("Now printing Arabic stopwords:")
print(arb_stopwords)