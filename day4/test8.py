cardNumber=input("WRite your card number: ")
lastNumberIndex=0
while cardNumber[lastNumberIndex:]:
    lastNumberIndex+=1

lastNumberIndex -=4
hidden="*"*(lastNumberIndex)
lastNumber=cardNumber[-4:]
result=hidden+lastNumber
print(result)