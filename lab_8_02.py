# lab_8_02.py
# Create a set of 10 random numbers between 15 and 45
# Count how many are less than 30, and delete numbers greater than 35

import random

numbers = {random.randint(15, 45) for _ in range(10)}
count_less_than_30 = sum(1 for n in numbers if n < 30)
numbers = {n for n in numbers if n <= 35}

print("Filtered Set:", numbers)
print("Count less than 30:", count_less_than_30)
