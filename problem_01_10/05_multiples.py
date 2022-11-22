"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the number from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def factorial(number):
    result = 1
    for i in range(1, number+1):
        result = result * i
    return result


def main():
    # just an assumed max. if no results before then it can be raised
    max = factorial(20)
    max_range = range(1, max)
    op_range = range(3, 20)
    for x in max_range:
        good_result = True
        if (x % 2 != 0):
            good_result = False
        else:
            for i in op_range:
                if (x % i != 0):
                    good_result = False
                    break
        if (good_result):
            print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is " + str(x))
            break


if __name__ == "__main__":
    main()
