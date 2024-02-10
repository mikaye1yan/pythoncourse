name=str(input("write your name "))

# if name=="Mubashir":
#     print("Hello," + "my Love")
# else:
#     print("Hello,"+ name)

msg=(name=="Mubashir")*("Hello, my Love") or (name!="Mubashir")*("Hello,"+name)
print(msg)