numbers = [1, 2, 3, 4, 5, 6]
zuyg = sum(num for num in numbers if num % 2 == 0)
kent= sum(num for num in numbers if num % 2 != 0)
print([zuyg, kent])