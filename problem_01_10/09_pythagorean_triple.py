"""
Special Pythagorean triplet
Problem 9

A Pythagorean triple is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000
Find the product abc.
"""

"""
Estimating C Maximum

a + b + c = 1000
re-arrange
c = 1000 - a - b
and
a < b < c
c is the largest number

c^2 = 1000^2 - 2000a - 2000b + a2 + 2ab + b2
OR
C^2 = 1,000,000 - some amount of a or b
"""
# Import math Library




import math
def digital_root_loop(number):
    save = 0
    mod = 0
    while number > 0:
        mod = number % 10
        save = save + mod
        number = number // 10
    return save


def pythagoren_c2(a, b):
    return (a*a) + (b*b)


def pythagoren_c(a, b):
    return math.sqrt(pythagoren_c2(a, b))


def main():
    for a in range(3, 1000):
        if (a % 100 == 0):
            print(str(a//10) + " Percent")
        for b in range(3, 1000):
            if (float(pythagoren_c2(a, b)).is_integer()):
                c = pythagoren_c(a, b)
                if (c.is_integer()):
                    if (a + b + (int(c)) == 1000):
                        print(a * b * c)
                        print(a)
                        print(b)
                        print(c)
                        return


if __name__ == "__main__":
    main()
