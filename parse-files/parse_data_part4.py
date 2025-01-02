import xml.etree.ElementTree as ET

file_path = "groceries.xml"

tree = ET.parse(file_path)
root = tree.getroot()

for item in root.findall("grocery_item"):
    name = item.find("name").text
    price = item.find("price").text
    print(name, price)

"""output:
Apples (per pound) 1.50
Bananas (per pound) 0.75
Oranges (per pound) 2.00
Plums (per pound) 1.80
Milk 2.49
Sour cream 1.79
Tortilla chips 2.49
Salsa 2.29
Carrots (per pound) 1.25
Broccoli (per pound) 2.50
Spinach (per bunch) 1.75
Avocados (per bag) 6.99
Cauliflower (per pound) 2.99
Blueberries (per pint) 3.99
Ketchup 1.49
Black beans (per can) 0.99
Bread 1.99
Cereal 3.29
Coffee (per pound) 7.99
Almonds (per pound) 6.99
Avocado Oil 14.49
Truffle Oil 18.99
Saffron (per gram) 15.99"""

items_over_6=[]
for item in root.findall("grocery_item"):
    price = float(item.find("price").text)
    if price > 6:
        items_over_6.append(item.find("name").text)

print("items with price higher than 6.00:",items_over_6)

"""output:
items with price higher than 6.00: ['Avocados (per bag)', 'Coffee (per pound)', 'Almonds (per pound)', 'Avocado Oil', 'Truffle Oil', 'Saffron (per gram)']"""