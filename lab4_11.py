# Calculate sin(x) using Taylor series
import math
x_deg = float(input("Enter angle in degrees: "))
x = x_deg * math.pi / 180  # convert to radians

def sin_taylor(x, terms=5):
    result = 0
    for i in range(terms):
        sign = (-1)**i
        result += sign * (x**(2*i + 1)) / math.factorial(2*i + 1)
    return result

print("sin(x) =", sin_taylor(x))
