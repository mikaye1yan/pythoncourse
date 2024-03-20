from time import perf_counter, sleep

def timer():
    start = perf_counter()
    def inner():
        sleep(3)
        return perf_counter() - start
    return inner


a = timer()
print(a())  
