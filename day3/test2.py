num=int(input("write only a two-digit number: "))
nish1=num//10
nish2=num%10
repdigit=(nish1==nish2) and num>0
print(repdigit)