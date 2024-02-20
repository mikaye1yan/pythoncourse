txt=input("Some text: ")
vowels=["a","e","i","o","u"]
count=0
for char in txt:
    if char in vowels:
        count +=1
        print("Number of vowels:", count)