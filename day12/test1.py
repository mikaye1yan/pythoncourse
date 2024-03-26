def type(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        res_type = type(res).__name__
        print("type:", res_type)
        return res
    return wrapper

@type
def type_function():
    return [1,5]

res = type_function()