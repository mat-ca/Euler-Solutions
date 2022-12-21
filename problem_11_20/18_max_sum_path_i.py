"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

That is, 3 + 7 + 4 + 9 = 23

Find the maximum total from top to bottom of the triangle below:
                   75
                  95 64
                 17 47 82
                18 35 87 10
               20 04 82 47 65
              19 01 23 75 03 34
             88 02 77 73 07 63 67
            99 65 04 28 06 16 70 92
           41 41 26 56 83 40 80 70 33
          41 48 72 33 47 32 37 16 94 29
         53 71 44 65 25 43 91 52 97 51 14
        70 11 33 28 77 73 17 78 39 68 17 57
       91 71 52 38 17 14 91 43 58 50 27 29 48
      63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

                   75
                  99 64
                 99 47 82
                99 35 87 10
               99 04 82 47 65
              99 01 23 75 03 34
             99 02 77 73 07 63 67
            99 65 04 28 06 16 70 92
           99 41 26 56 83 40 80 70 33
          99 48 72 33 47 32 37 16 94 29
         99 71 44 65 25 43 91 52 97 51 14
        99 11 33 28 77 73 17 78 39 68 17 57
       99 71 52 38 17 14 91 43 58 50 27 29 48
      99 66 04 68 89 53 99 30 73 16 69 87 40 31
    02 62 98 27 23 09 70 99 73 93 38 53 60 04 23

Note: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, problem 67 is the same challenge with a triangle containing 100 rows.
It cannot be solved by brute force and requires a clever method! ;o)
"""


def read_tree_string(tree_str):
    # Read a string with a pyramid numerical structure, and
    # return it as a list of the values
    return [[int(y) for y in x.split()] for x in tree_str.split("\n")]


def climb_tree(tree):
    # Given a tree structure, search from the bottom up
    # count the sum of path
    # return the sum and the numerical values of the path
    row_index = len(tree) - 1  # -1 to account that it is an index
    for i in range(row_index, -1, -1):  # count up from lowest row in tree
        print(tree[i])
        rx_cnt = len(tree[i])
        for x in range(0, rx_cnt - 1):
            cur = tree[i][x]
            cpo = tree[i][x + 1]
            if (cur > cpo):
                print("out of " + str(cur) + " and " +
                      str(cpo) + " winner " + str(cur))
                if i > 0:
                    tree[i-1][x] += cur
            else:
                print("out of " + str(cur) + " and " +
                      str(cpo) + " winner " + str(cpo))
                if i > 0:
                    tree[i-1][x] += cpo


def main():
    simple_tree_str = \
        """3
7 4
2 4 6
8 5 9 3"""
    tree_str = \
        """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
    tree = read_tree_string(tree_str)
    climb_tree(tree)


if __name__ == "__main__":
    main()
