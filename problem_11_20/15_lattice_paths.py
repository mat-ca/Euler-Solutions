"""
Lattice Paths
Problem 15

Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

    __     _        _
      |     |_       |
      |       |      |_

    |__     |_      |
       |      |_    |__

How many such routes are there through a 20x20 grid?


*****
The following notes are based on a grid where the cell is moving, while the original question asks about moving along the axis.
Essentially add 1 when talking about moving along the axis, eg:
    3x3 grid along the cells
        equals
    2x2 grid along the axis
***

First note that the number of steps we have to take doesn't depend on the path taken.

The distance, measured in steps, is always the same.

This distance is also called the L1 distance, city block distance, manhattan distances.

The number of down moves is equal to the number of right moves due to symmetry.

20 + 20 = 40 moves in every path.

These two requirements make it possible to redefine the problem for the 20x20 grid in the following way:

Find the number of distinct permutations of the string DDDDDDDDDDDDDDDDDDDDRRRRRRRRRRRRRRRRRRRR

The number of permutations is defined as factorial(number)

For us fact(20)

We have to account for the fact that the order of the R's and D's doesn't matter - they are the same.
The number of different permutations of D is fact(10)
The number of different permutations of R is fact(10)

Therefore our equation is
factorial(number) / (factorial(number/2)^2)

"""


def factorial(number):
    result = 1
    for i in range(1, number+1):
        result = result * i
    return result


def main():
    print(factorial(40)//(factorial(20) * factorial(20)))


if __name__ == "__main__":
    main()
