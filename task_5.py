# task 1

# Step 1: Iterate over the numbers from 1 to 50
# for num in range(1, 51):
#     # Step 2: Check if the number is a multiple of both 3 and 5
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     # Step 3: Check if the number is a multiple of 3
#     elif num % 3 == 0:
#         print("Fizz")
#     # Step 4: Check if the number is a multiple of 5
#     elif num % 5 == 0:
#         print("Buzz")
#     # Step 5: If the number is not a multiple of 3 or 5, print the number itself
#     else:
#         print(num)






# task 2


import random

# Get desired password length from the user
password_length = int(input("Enter the desired password length: "))
# Define characters for the password
digits = ["0","1","2","3","4","5","6","7","8","9"]
uppercase_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercase_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
special_characters =["!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","|",";",":","<",">","/","?"] 
# Combine all character sets
all_characters = digits + uppercase_letters + lowercase_letters + special_characters
# Generate password using a list
generated_password = ''
for _ in range(password_length):
    generated_password += random.choice(all_characters)

print("Generated Password:", generated_password)

