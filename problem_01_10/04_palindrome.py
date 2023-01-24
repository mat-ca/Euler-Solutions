"""
Largest palindrome product
Problem 4

A palindromic number reads the same both forwards and backwards.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def reverse_number(num):
    """
    we are going to use mod 10 to chop numbers up
    Given the number 1234, we want 4321 - SO
    1234 % 10 = 4
    save = save * 10 + 4
    1234 // 10 = 123
    loop
    :param num: the number to reverse
    :return: the reversed number
    """
    save = 0
    mod = 0
    while num > 0:
        mod = num % 10
        save = save * 10 + mod
        num = num // 10
    return save


def is_palindrome_number(num):
    """
    Given a number, determine if it is palindromic
    :param num: the number to check
    :return: true = is palindrome, false = is not palindrome
    """
    return num == reverse_number(num)


def main():
    result = 0
    op_x = 0
    op_i = 0
    number_range = range(100, 999)
    for x in number_range:
        for i in number_range:
            if (is_palindrome_number(x*i) & (x*i > result)):
                result = (x*i)
                op_x = x
                op_i = i
        if (x == 990):
            print()
    print("That largest palindrom made from two three-digits numbers is: " +
          str(result) + "=" + str(op_x) + "x" + str(op_i))


if __name__ == "__main__":
    main()
