items = []

while True:
    item = input('Add an item (type "exit" to stop): ')
    if item == 'exit':
        break
    items.append(int(item))

sumOfItems = sum(items)
print(f"The sum of the items is: {sumOfItems}")
