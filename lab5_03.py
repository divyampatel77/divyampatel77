# Program 3
import random

nums = [random.randint(1, 30) for _ in range(50)]
print("Original list:", nums)
unique_nums = list(set(nums))
print("List after removing duplicates:", unique_nums)
