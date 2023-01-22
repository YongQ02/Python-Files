import wikipedia

wikipedia.set_lang("zh")
topic = wikipedia.page("原神")
print(topic.content[0:5000])
print(topic.images[0:10])