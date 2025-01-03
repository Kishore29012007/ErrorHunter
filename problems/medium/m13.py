'''
Create a program that checks whether a given number is a prime number or not.
'''
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
for i in range(2, n + 1):
    if is_prime(i):
        print(i)
