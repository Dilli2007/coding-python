# Program to count the number of vowels in a string (no loops or ifs)

s = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = sum(s.count(v) for v in vowels)

print(f"Number of vowels in '{s}' is: {vowel_count}")
