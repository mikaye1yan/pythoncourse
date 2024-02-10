a=int(input("write a single digit number"))
b=int(input("write another single digit number"))

# if a==10:
#     print("True")
# elif b==10:
#     print("True")
# elif a+b==10:
#     print("True")
# else:
#     print("False")


result=(a==10)*("True") or (b==10)*("True") or (a+b==10)*("True") or "False"
print(result)