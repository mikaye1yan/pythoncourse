def pluralize(words):
    pluralWords = set()
    for word in set(words):
        if words.count(word) > 1:
            pluralWords.add(word + "s")
        else:
            pluralWords.add(word)
    return pluralWords
print(pluralize(["cow", "pig", "cow", "cow"]))  
print(pluralize(["table", "table", "table"]))  
print(pluralize(["chair", "pencil", "arm"]))   