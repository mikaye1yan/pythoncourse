"2.	Create a function that takes two arguments. Both arguments are integers,  a and b. Return True if one of them is 10 or if their sum is 10.Examples a,b = 9, 10 ➞ True a,b = 9, 9 ➞ False"
a = int(input("number 1 "))
b = int(input("number 2 "))
result = (a == 10 or b == 10) or (a + b == 10)
print(result)