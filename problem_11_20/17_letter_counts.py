"""
Number Letter Counters
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five
Then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters.
115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.




hundred and

mod = number mod 10
number // ten



"""
singles = ["",
           "one",
           "two",
           "three",
           "four",
           "five",
           "six",
           "seven",
           "eight",
           "nine"]
teens = ["ten",
         "eleven",
         "twelve",
         "thirteen",
         "fourteen",
         "fifteen",
         "sixteen",
         "seventeen",
         "eighteen",
         "nineteen"]
tens = ["",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety"]

# for i in range(0, 9):
#    print(singles[i])


def main():
    letter_count = 0
    for number in range(1, 1001):
        loop_string = ""
        # Check if number will need "and", as in:
        # One hundred AND fifteen
        if number >= 100 and number % 100 != 0:
            loop_string = loop_string + "and"
        # First check if number in teens range - special case
        if (number % 100) // 10 % 10 == 1:
            loop_string += teens[number % 10]
            # both the last two digits are dealt with - remove for future checks
            number = number // 100
            number = number * 100
        # Add single digit to iterative string
        loop_string = loop_string + singles[number % 10]
        number = number // 10
        loop_string = loop_string + tens[number % 10]
        number = number // 10
        if number != 0 and number < 10:
            loop_string = loop_string + singles[number] + "hundred"
        number = number // 10
        if number != 0 and number < 10:
            loop_string = loop_string + singles[number] + "thousand"
        letter_count += len(loop_string)
    print(letter_count)


if __name__ == "__main__":
    main()
