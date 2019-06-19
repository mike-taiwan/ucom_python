import wikipedia

print wikipedia.summary("Pythonidae")
print wikipedia.summary("Python")
print wikipedia.search("C++")
taipei = wikipedia.page("Taipei")
print taipei.url, taipei.title
#print taipei.links[:2]
for link in taipei.links[:5]:
    print link
print taipei.content
wikipedia.set_lang("zh")
print wikipedia.summary("Taipei", sentences=3)