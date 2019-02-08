from xml.dom import minidom
import re

MAX_ROWS = 200

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

# parse an xml file by name
mydoc = minidom.parse('Anime.xml')

items = mydoc.getElementsByTagName('row')
index=0
wordmap = {}

count=0

for item in items:
    count=count+1
    if count==MAX_ROWS:
        break
    string = remove_tags(item.attributes['Body'].value)
    words = string.split(" ")
    for word in words:
        # print(word)
        if word not in wordmap:
            wordmap[word] = index
            index = index + 1

print(len(wordmap))

vector = [0]*len(wordmap)
testdoc = minidom.parse('Anime.xml')

testItems = mydoc.getElementsByTagName('row')
string = remove_tags(testItems[0].attributes['Body'].value)
print(string)
words = string.split(" ")
for w in words:
    if w in wordmap.keys():
        vector[wordmap[w]]=vector[wordmap[w]]+1
        if vector[wordmap[w]]>=2:
            print(w)

print(vector)