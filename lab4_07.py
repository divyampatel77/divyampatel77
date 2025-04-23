# Print nCr and nPr
import math
n = int(input("Enter n: "))
r = int(input("Enter r: "))
nCr = math.comb(n, r)
nPr = math.perm(n, r)
print("nCr:", nCr)
print("nPr:", nPr)
