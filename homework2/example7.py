items = []

while True:
    item = input('add an item: ')
    if item == '0':
        break
    items.append(item)

print(len(items))