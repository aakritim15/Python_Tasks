# import random
# def generatePassword(n):
#     characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?/+-"
#     password = ""
#     for i in range(n):
#         password += random.choice(characters)
#     return password

# if __name__ == "__main__":
#     n = int(input("Enter the length of password:"))
#     password = generatePassword(n)
#     print("A randomly generated password is:", password)


import random
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case="abcdefghijklmnopqrstuvwxyz"
numbers ="0123456789"
symbols = "!@#$%^&*()+-/?"
print("Welcome to the Password Generator!")
n=int(input("Enter length of password:\n"))
pwd_uc= int(input("How many upper case letters would you like to have in your password?\n"))
pwd_lc= int(input("How many lower case letters would you like to have in your password?\n"))
pwd_s = int(input(f"How many symbols would you like to have in your password?\n"))
pwd_n = int(input(f"How many numbers would you like to have in your password?\n"))
if(n==(pwd_uc+pwd_lc+pwd_s+pwd_n)):    
    password_list = []
    for char in range(1, pwd_uc + 1):
        password_list.append(random.choice(upper_case))
    for char in range(1, pwd_lc + 1):
        password_list.append(random.choice(lower_case))
    for char in range(1, pwd_s + 1):
        password_list.append(random.choice(numbers))
    for char in range(1, pwd_n + 1):
        password_list.append(random.choice(symbols))
    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    pwd = ''.join(password_list)
    print(f"Your random password generated is: {pwd}")
else:
    print("The password length does not meet the requirements given for the specifications.")
