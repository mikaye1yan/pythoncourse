def consecutive_combo(lst1, lst2):
    comb = sorted(lst1 + lst2)
    return all(comb[i] == comb[i-1] + 1 for i in range(1, len(comb)))
print(consecutive_combo([7, 4, 5, 1], [2, 3, 6])) 
print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))  
print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))  
print(consecutive_combo([44, 46], [45]))  