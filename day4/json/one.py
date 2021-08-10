import json

with open("example_1.json") as fj:
    data = json.load(fj)

print(data)
print(type(data))
