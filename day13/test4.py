data = [
    {"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
    {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}
]
values = [val for d in data for val in d.values()]
uniqueValues = set(values)
print("Unique Values:", uniqueValues)