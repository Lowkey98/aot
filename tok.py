import nltk
import string
from nltk.stem import WordNetLemmatizer 

nltk.download('wordnet')
file_content = open("aot01").read()
file_content = file_content.translate(string.punctuation)
characters_to_replace = "."


for character in characters_to_replace:
    str = file_content.replace(character, " ")


removed_words = ['...','you']
lemmatizer = WordNetLemmatizer()
tokens = nltk.word_tokenize(str)
tokens = list(filter(lambda token: token not in string.punctuation , tokens))
tokens = list(filter(lambda token: token  not in removed_words, tokens))

tokens = [token.replace('+','').lower() for token in tokens]
tokens = [lemmatizer.lemmatize(token) for token in tokens]

#print(token)
from collections import Counter
  
Counter = Counter(tokens)
#print(tokens)
# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(10000)
  
print(most_occur)
