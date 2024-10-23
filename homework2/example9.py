x = input('Type a word: ')

if x.lower() == x[::-1].lower():
    print('palindrome')
else:
    print('Not a palindrome')
