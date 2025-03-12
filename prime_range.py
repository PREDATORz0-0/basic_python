"""
Write a Python program that takes two numbers, start and end, and prints all prime numbers in that range.

Example:
  For start = 10, end = 30:
  11, 13, 17, 19, 23, 29
"""""""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=', ')

start=int(input("ENTER THE START NUMBER : "))
end=int(input("ENTER THE END NUMBER : "))
primes_in_range(start, end)
