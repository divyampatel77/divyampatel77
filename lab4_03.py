# Count number of alphabets and digits in a given string
text = input("Enter a string: ")
alphabets = sum(c.isalpha() for c in text)
digits = sum(c.isdigit() for c in text)
print("Alphabets:", alphabets)
print("Digits:", digits)
