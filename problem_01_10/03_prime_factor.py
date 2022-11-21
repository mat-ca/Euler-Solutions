"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
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


def find_first_prime_factor(number):
    for x in range(1, number):
        if (number % x == 0):
            # x is factor of number
            if (is_prime(x)):
                # x is a prime factor of number
                return x


def main():
    pf_list = []
    number = 600851475143
    while find_first_prime_factor(number):
        x = find_first_prime_factor(number)
        pf_list.append(x)
        number = number // x
        if (is_prime(number)):
            pf_list.append(number)
            break
    print("The prime factors of 600851475143 are: " + str(pf_list))


if __name__ == "__main__":
    main()
