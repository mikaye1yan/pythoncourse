txt = input("Enter some text: ")
n = int(input("Enter a number: "))

if type(txt) == str:
    print(txt * n)
else:
    print("Not a string")


# result=(type(txt)==str)*(txt*n) or "Not a string"
# print(result)