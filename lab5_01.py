# Program 1
import random

odd_list = random.sample(range(1, 100, 2), 5)
even_list = random.sample(range(2, 100, 2), 4)
print("Original odd list:", odd_list)
print("Even list:", even_list)

odd_list[2] = even_list
print("After replacing 3rd element with even list:", odd_list)

# Flatten
flattened = []
for item in odd_list:
    if isinstance(item, list):
        flattened.extend(item)
    else:
        flattened.append(item)
print("Flattened list:", flattened)

# Sort and print
flattened.sort()
print("Sorted list:", flattened)
