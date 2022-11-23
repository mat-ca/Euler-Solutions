"""
10,001st Prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""


def is_prime(number):
    # Given a number, check if it is prime.
    # Returns true = is prime, returns false, is not prime
    prime_count = 0
    for x in range(1, number + 1):
        if (number % x == 0):
            prime_count += 1
            if (prime_count > 2):
                return False
    return (prime_count == 2)


def main():
    prime_count = 2  # skip 2 and 3 - start iterator at 5 (3 + 2)
    i = 3
    while prime_count < 10001:
        i += 2  # Skip 2 - avoid even non prime numbers
        if (is_prime(i)):
            prime_count += 1
    print(str(prime_count) + " " + str(i))


if __name__ == "__main__":
    main()
