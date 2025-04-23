# lab_8_01.py
# Convert words in a list to uppercase and store in a set

words = ["apple", "banana", "grape", "apple", "banana"]
uppercase_set = {word.upper() for word in words}

print("Uppercase Set:", uppercase_set)
