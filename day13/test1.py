def rep_set(n):
    result = []
    for i in range(n):
        result.append(result[:])
    return result
print(rep_set(0))  
print(rep_set(1))  
print(rep_set(2)) 
print(rep_set(3))  