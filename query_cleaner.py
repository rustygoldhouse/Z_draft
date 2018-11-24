from textblob import TextBlob
import unicodedata
import contractions
import re

def remove_accented_chars(text_source):
    text = unicodedata.normalize('NFKD', text_source).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

def remove_special_characters(source_txt, remove_digits=False):
    pattern = r'[^a-zA-z0-9\s]' if not remove_digits else r'[^a-zA-z\s]'
    text = re.sub(pattern, '', source_txt)
    return text


query = 'what would i be if my heart were comprised of fear and trembled like thunder?'
xpand = contractions.fix(query)
trim = remove_special_characters(xpand)
text = remove_accented_chars(trim)

blob = TextBlob(text)

terms = []

for word, pos in blob.tags:
    if pos == 'NN':
        terms.append(word)
    elif pos == 'VB':
        terms.append(word)
    elif pos == 'JJ':
        terms.append(word)

print(terms)

#print(blob.noun_phrases)