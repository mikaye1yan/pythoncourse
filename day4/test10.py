string1 = 'Algorism'
string2 = 'PasSword'
string3 = 'Consecutive'
is_isogram1 = True
is_isogram2 = True
is_isogram3 = True
for i in range(len(string1)):
    for j in range(i + 1, len(string1)):
        if string1[i] == string1[j]:
            is_isogram1 = False
for i in range(len(string2)):
    for j in range(i + 1, len(string2)):
        if string2[i] == string2[j]:
            is_isogram2 = False
for i in range(len(string3)):
    for j in range(i + 1, len(string3)):
        if string3[i] == string3[j]:
            is_isogram3 = False
print(is_isogram1) 
print(is_isogram2)  
print(is_isogram3)  
