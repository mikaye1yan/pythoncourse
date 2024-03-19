def matrix(x, y, z):
    return [[z] * y for _ in range(x)]
print(matrix(3, 2, 3))     
print(matrix(2, 1, "edabit")) 
print(matrix(3, 2, 0))       