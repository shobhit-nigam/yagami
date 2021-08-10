import json

with open("example_2.json") as fj:
    data = json.load(fj)

#print(data)
print(data['quiz']['maths']['q1'])
