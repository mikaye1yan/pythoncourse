txt = input("Write string: ")
char = input("replace vowels with: ")
vowels = 'aeiouAEIOU'
modifiedString = ''

for i in txt:
    if i in vowels:
        modifiedString += char
    else:
        modifiedString += i

print(modifiedString)