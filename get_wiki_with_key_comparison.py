

import wikipedia
from newspaper import Article, Config
from keywords import KeyWords
#from nltk.corpus import stopwords

wikipedia.set_lang("en")

def usr_query(topic):
    search = topic
    return search


query = input("what's on your mind? ")
terms = query.split(' ')

pages = []

for item in terms:
    search = wikipedia.search(item)
    pages.extend(search)

data = ' '.join(pages)

print(data)


with open('Z_draft/key_word_extract/corpus.txt', 'r', encoding="utf8") as f:
    corpus_1 = f.read()

keyword = KeyWords(corpus=corpus_1, alpha=0.8)
d = keyword.get_keywords(data, n=20)

file = open('keys.txt', 'w')


for i in d:
    file.write(i[0])
    file.write('\n')

file.close()

with open('keys.txt', 'r') as file:
    keys=file.read()

print(keys)

pages = keys.split()


# here is where i procecss the terms for compatibilty with pretrained models

file = open("wiki_text.txt", "w")
file.close()

file = open("wiki_text.txt", "a")

config = Config()
config.MAX_KEYWORDS=20
config.MAX_SUMMARY=3000
config.MAX_TEXT=50000

for item in pages:
    try:
        raw = wikipedia.page(item)
        link = raw.url
        article = Article(link, language='en', request_timeout=3, memoize_articles=False)
        article.download()
        article.parse()
        article.nlp()
        """
        text = article.text
        file.write('\n---> text 15\n')
        file.write(text[:500])
        """
        file.write('\n---> summary\n')
        file.write(article.summary)
        file.write('\n---> key word\n')
        keys = article.keywords
        file.write(' '.join(keys))
    except wikipedia.exceptions.DisambiguationError:
        pass

file.close()

with open('wiki_text.txt', 'r') as f:
    result = f.read()


print(result)