vowels = "aeiouAEIOU"
count = 0

user_input = input("Enter a string: ")

    
for char in user_input:
    if char in vowels:
        count += 1
    
print(f"The number of vowels in the string is: {count}")
