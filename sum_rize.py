from summa import keywords
from summa.summarizer import summarize

with open('Z_draft/key_word_extract/script.txt') as f:
    text = f.read()

print(summarize(text, ratio=0.2))


print(keywords.keywords(text))
