def intWithinBounds(n, lower, upper):
    return isinstance(n, int) and lower <= n < upper
print(intWithinBounds(3, 1, 9))    
print(intWithinBounds(6, 1, 6))    
print(intWithinBounds(4.5, 3, 8))  
