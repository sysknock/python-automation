file_path = "groceries.txt"

with open(file_path, "r") as file:
    data = file.read()
    
print("data:", data)
parsed_data = data.split(", ") #comma with space as separators
print("parsed data:", parsed_data)
print("item at index 2:", parsed_data[2])

"""output:
data: apples, bananas, carrots, durians, eggplants, ginger, hazelnuts
parsed data: ['apples', 'bananas', 'carrots', 'durians', 'eggplants', 'ginger', 'hazelnuts']
item at index 2: carrots"""

"""output of comma without space seperator:
data: apples, bananas, carrots, durians, eggplants, ginger, hazelnuts
parsed data: ['apples', ' bananas', ' carrots', ' durians', ' eggplants', ' ginger', ' hazelnuts']
item at index 2:  carrots"""