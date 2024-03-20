def accumulating_list(s):
    summ=0
    l=[]
    for i in s:
        summ=summ +i
        l.append(summ)
    return l 

print(accumulating_list([1, 2, 3, 4]))
print(accumulating_list([1, 5, 7]))
print(accumulating_list([1, 0, 1, 0, 1]))
print(accumulating_list([]))