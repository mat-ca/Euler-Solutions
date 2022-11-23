"""
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
    (1_2_...+10)^2 = 55^2 = 3025
Hence the difference between the sum of the first ten natural numbers and the square of the sum is 3025 - 385 - 2640.

Find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum.
"""

"""
Sum of N Squares
1/3n^3 + 1/2n^2 + 1/6n
Khan Academy "Finding the sum of n squares"
https://www.youtube.com/watch?v=i7iKLZQ-vCk
"""


def sum_of_n_sqrs(number):
    n = number
    nn = n * number
    nnn = nn * number
    return (((1/3)*nnn)+((1/2)*nn)+((1/6)*n))


"""
Square of the sum of N numbers
((n(n+1))/2)
Sum of N number: Stack Exchange "Factorial, but with addition"
https://math.stackexchange.com/questions/593318/factorial-but-with-addition
https://i1115.photobucket.com/albums/k544/akinuri/nth%20triangle%20number-01.jpg
"""


def sqr_of_n_sum(number):
    sum = ((number*(number+1))/2)
    return sum * sum


def main():
    print("The difference between the sum of the squares of the first 100 natural numbers and the square of the sum is " +
          str(sqr_of_n_sum(100) - sum_of_n_sqrs(100)))


if __name__ == "__main__":
    main()
