# Write a program that computes the prime number from 1 to N.
# A prime number is a number only divisible by 1 and itself

def prime_number(n):
    if (n==0):
        return False
    for i in range(2, n):
        if (n%i==0):
            return False
    return True

n = 10
for i in range(1, n+1):
    if (prime_number(i)):
        print(i, end=" ")
