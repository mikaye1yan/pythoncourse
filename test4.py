"4.	Create a function that takes a number as an argument and returns negative of that number. Return negative numbers without any change."
num = float(input("Enter a number: "))
result = num * (-1) ** (num != 0)
print("Result:", result)
