def censor(sentence):
    words = sentence.split()
    censored_words = [word if len(word) <= 4 else '*' * len(word) for word in words]
    return ' '.join(censored_words)
print(censor('Two plus three is five'))  
print(censor('aaaa aaaaa 1234 12345'))   