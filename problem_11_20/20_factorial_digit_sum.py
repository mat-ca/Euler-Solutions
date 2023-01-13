"""
Factorial Digit Sum
Problem 20

n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x 8 ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

find the sum of the digits in the number 100!
"""


def factorial(number):
    result = 1
    for i in range(1, number+1):
        result = result * i
    return result


def main():
    fact_res = factorial(100)
    sum = 0
    while fact_res:
        sum = sum + (fact_res % 10)
        fact_res = fact_res // 10
    print(sum)


if __name__ == "__main__":
    main()
