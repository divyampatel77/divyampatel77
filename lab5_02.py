# Program 2
import random

nums = [random.randint(1, 100) for _ in range(20)]
print("Generated list:", nums)
target = int(input("Enter a number to find its positions: "))
positions = [i for i, x in enumerate(nums) if x == target]
print(f"Positions of {target}:", positions)
