"""
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math


def is_prime(number):
    # Given a number, check if it is prime.
    # Returns true = is prime, returns false, is not prime
    prime_count = 0
    for x in range(1, math.floor(math.sqrt(number)) + 1):
        if (number % x == 0):
            prime_count += 1
            if (prime_count > 1):
                return False
    return (prime_count == 1)


def main():
    count = 2
    for x in range(3, 2000000, 2):
        if (is_prime(x)):
            count = count + x
    print(count)


if __name__ == "__main__":
    main()
