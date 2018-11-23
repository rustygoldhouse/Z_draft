from keywords import KeyWords
from nltk.corpus import stopwords

with open('Z_draft/key_word_extract/script.txt', 'r') as f:
    data = f.read()

with open('Z_draft/key_word_extract/transcript_1.txt', 'r', encoding="utf8") as f1:
    corpus_1 = f1.read()

stopWords = stopwords.words('english')
keyword = KeyWords(corpus=corpus_1, stop_words=stopWords, alpha=0.8)
d = keyword.get_keywords(data, n=20)

file = open('keys.txt', 'w')

for i in d:
    file.write(i[0])
    file.write('\n')

file.close()

with open('keys.txt', 'r') as file:
    keys=file.read()

print(keys)