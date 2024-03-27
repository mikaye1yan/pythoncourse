def count_datatypes(*args):
    return [sum(isinstance(arg, datatype) for arg in args) for datatype in (int, str, bool, list, tuple, dict)]
print(count_datatypes(True))