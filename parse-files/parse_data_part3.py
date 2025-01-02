import json

file_path = "groceries.json"

with open(file_path, "r") as file:
    data = file.read()

parsed_data = json.loads(data)
print(parsed_data)

print("apples quantity:", parsed_data["apples"])

"""output:
{'apples': 2, 'bananas': 6, 'carrots': 4, 'durians': 3, 'eggplants': 5, 'ginger': 1, 'hazelnuts': 8}
apples quantity: 2"""