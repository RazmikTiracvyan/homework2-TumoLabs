number = int(input('type a number: '))

isValid = False

for i in range(2, number):
    if number % i == 0:
        isValid = True
        break

if isValid:
    print('baghadryal')
else:
    print('parz')