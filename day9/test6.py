from functools import reduce


def mult(a):
    return reduce(lambda x,y:x*y,a)
b=[[1,2,3],[4,5,6],[7,8,9]]
c=[d for e in b for d in e]
print(mult(c))