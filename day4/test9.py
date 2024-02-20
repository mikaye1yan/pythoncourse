fullName= input("write name and surname: ")
space=fullName.index(" ")
name=fullName[:space]
surname=fullName[space+1:]
result=name+" "+surname
print(result)