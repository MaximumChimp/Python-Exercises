#PROBLEM: Write a program to find all prime numbers up to 20, but only print every second (alternate) prime number found.
#PURPOSE: This exercise combines “Nested Loops” (to check for primality) with “Step Logic.” It requires the programmer to first identify a subset of data and then apply a secondary filter, a common task in data reporting.

primes = []
def check_prime_numbers(n):
    for num in range(2, 21): # Start at 2, as 1 is not prime
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)



check_prime_numbers(20)

new_list = primes[::2]

print(new_list)