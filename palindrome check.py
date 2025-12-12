# Program to check if a number is palindrome

num = int(input("Enter a number: "))   #121
temp = num
reverse = 0

while temp > 0:   #T  #12 T  #1T #false
    digit = temp % 10   #1 #2  #1
    reverse = reverse * 10 + digit  #1 #12  #121
    temp //= 10   #12  #1  #0.1

if num == reverse: #true
    print(f"{num} is a Palindrome number.")
else:
    print(f"{num} is not a Palindrome number.")
