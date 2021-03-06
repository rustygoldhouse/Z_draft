import wikipedia
from newspaper import Article, Config


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
        file.write('\n---> summary\n')
        file.write(article.summary)
        """
        file.write('\n---> key words\n')
        keys = article.keywords
        file.write(' '.join(keys))
    except wikipedia.exceptions.DisambiguationError:
        pass

file.close()

with open('wiki_text.txt', 'r') as f:
    result = f.read()


print(result)





