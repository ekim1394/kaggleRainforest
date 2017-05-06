'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''
import pandas as pd
import csv

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''
r = open ('C:\Users\simpl\Documents\ds-dc-19\dataset/chipotle.tsv', 'rb')
file_nested_list = csv.reader(r, delimiter='\t')
file_nested_list

'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''
header = file_nested_list.next()
data = []
firstLine = True
for row in file_nested_list:
    if firstLine:
        firstLine = False
        continue
    data.append(row)

header
data
'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''
sum = 0
total = 0
for i, row in enumerate(data):
    sum += float(data[i][1]) * float(data[i][4][1:-1])
    total += 1
average = sum/total
average
'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''
data[0:5]
header
drinks = []
for i, row in enumerate(data):
    if data[i][2] == 'Canned Soda' or data[i][2] == 'Canned Soft Drink':
        if data[i][3] not in drinks:
            drinks.append(data[i][3])

drinks

'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''

topCnt = 0
burritoCnt = 0
for i, row in enumerate(data):
    if "Burrito" in data[i][2]:
        burritoCnt += 1
        for n in data[i][3].split(','):
             topCnt += 1

mean = topCnt/burritoCnt
mean
'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''
chipOrders = {}

# Init Dictionary with 0 values but all chips
for i, row in enumerate(data):
    if 'Chips' in data[i][2]:
        if data[i][2] not in chipOrders:
            chipOrders.update({data[i][2]:0})
        else:
            continue

# Count all Chip Values
for i, row in enumerate(data):
    if 'Chips' in data[i][2]:
        chipOrders[data[i][2]] += 1 * int(data[i][1])

chipOrders
'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''
