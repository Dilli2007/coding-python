#password generator

import random

pasw = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890.,/';[]@#$%^&*()_+~`<>?-=|"

use = input("Enter the website to use password:   ")

PASSWORD = ""

try:
    want = int(input("Enter length you want:"))
except ValueError as v:
    print("Invalid integer")
else:
    for i in range(want):
        char = random.choice(pasw)
        #print(i)
        #print('here is you use this password')
        #print(char, end="")
        PASSWORD = PASSWORD + char
    
    # print("Your strong password is ")
    # print(PASSWORD)
    data = f"\nYour password for {use} is {PASSWORD}"
    print(data)

    file = open("passwordGenerator.txt",'a')
    # file1 = open("hello world.py",'a')
    file.write(data)
    file.close()
finally:
    print("Program terminated")




