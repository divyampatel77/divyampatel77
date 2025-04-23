# Check properties of a number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    return n == sum(int(d)**len(str(n)) for d in str(n))

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    return str(n**2).endswith(str(n))

num = int(input("Enter a number: "))
print("Prime:", is_prime(num))
print("Perfect:", is_perfect(num))
print("Armstrong:", is_armstrong(num))
print("Palindrome:", is_palindrome(num))
print("Automorphic:", is_automorphic(num))
