num=int(input("write some number: "))

# if num%2==0:
#     print("even")
# else:
#     print("odd")

result=(num%2==0)*"even" or (num%2!=0)*"odd"
print(result)