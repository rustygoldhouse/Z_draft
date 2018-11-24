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

file = open("wiki_text.txt", "w")
file.close()

file = open("wiki_text.txt", "a")


for item in pages:
    try:
        raw = wikipedia.page(item)
        link = raw.url
        article = Article(link, language='en')
        article.download()
        article.parse()
        article.nlp()
        text = article.text
        file.write('\n---> text 15')
        file.write(text[:15])
        file.write('\n---> summary')
        file.write(article.summary)
        file.write('\n---> key words')
        file.write(article.keywords)
    except wikipedia.exceptions.DisambiguationError:
        pass

file.close()

with open('wiki_text.txt', 'r') as f:
    result = f.read


print(result)


