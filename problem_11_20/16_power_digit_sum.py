"""
Power Digit Sum
Problem 16

2 ^ 15 = 32768 and the sum of it's digit is 3+2+7+6+8=26

What is the sum of the digits of the number 2 ^ 1000?
"""


def sum_number(num):
    """
    we are going to use mod 10 to chop numbers up
    Given the number 1234, we want 1+2+3+4 - SO
    1234 % 10 = 4
    save = save + 4
    1234 // 10 = 123
    loop
    """
    save = 0
    mod = 0
    while num > 0:
        mod = num % 10
        save = save + mod
        num = num // 10
    return save


def main():
    print(sum_number(1 << 1000))


if __name__ == "__main__":
    main()
