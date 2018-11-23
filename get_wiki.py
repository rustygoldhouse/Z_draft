import wikipedia
from newspaper import Article
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

file = open("Z_draft/key_word_extract/script.txt", "w")
file.close()

file = open("Z_draft/key_word_extract/script.txt", "a")

summs = open("Z_draft/key_word_extract/transcript_1.txt", "w")
summs.close()

summs = open("Z_draft/key_word_extract/transcript_1.txt", "a")

for item in pages:
    try:
        raw = wikipedia.page(item)
        link = raw.url
        article = Article(link)
        article.download()
        article.parse()
        article.nlp()
        text = article.text
        file.write(text)
        summs.write(article.summary)
    except wikipedia.exceptions.DisambiguationError:
        pass

file.close()
summs.close()









