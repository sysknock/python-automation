import csv

file_path = "groceries.csv"

with open(file_path, "r") as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader) #to separate the data from headers
    for row in csv_reader:
        row[1] = int(row[1]) #to print the quantity as integer instead of string
        print(row)

"""output:
['apples', 2]
['bananas', 6]
['carrots', 4]
['durians', 3]
['eggplants', 5]
['ginger', 1]
['hazelnuts', 8]"""

"""output of not changing to int:
['apples', '2']
['bananas', '6']
['carrots', '4']
['durians', '3']
['eggplants', '5']
['ginger', '1']
['hazelnuts', '8']"""