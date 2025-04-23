# Program 4
import random

nums = [random.randint(-50, 50) for _ in range(30)]
positives = [x for x in nums if x > 0]
negatives = [x for x in nums if x < 0]
print("Original list:", nums)
print("Positive numbers:", positives)
print("Negative numbers:", negatives)
