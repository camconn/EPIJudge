from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    mat = partial_assignment
    
    height = 9
    width = 9

    # check horizontal consistency
    for i in range(height):
        row = mat[i]
        for j in range(width):
            elem = row[j]
            if elem == 0: continue

            if elem in row[0:j] or \
               elem in row[j+1:]:
                return False

    # check vertical consistency
    for j in range(width):
        col = []
        for i in range(height):
            elem = mat[i][j]
            if elem == 0: continue

            if elem in col:
                return False

            col.append(elem)

    # check 9x9 consistency
    # this is technically just goes to 7, but we need 7 inclusive, hence +1
    for j in range(1, 7+1, 3):
        for i in range(1, 7+1, 3):

            group = []
            # go up 1 and down 1 and left one and right one from (i, j) so we get
            # a "group" of 9 squares (a 3x3)
            for y in range(j-1, j+2):
                for x in range(i-1, i+2):
                    elem = mat[y][x]
                    if elem == 0: continue

                    if elem in group:
                        return False
                    group.append(elem)

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))



#[
#   [0, 0, 0,    0, 0, 0,    0, 0, 0],
#   [0, 0, 0,    0, 0, 6,    0, 0, 0],
#   [0, 0, 0,    0, 0, 0,    0, 0, 0],

#   [0, 0, 0,    0, 8, 0,    0, 0, 0],
#   [9, 0, 0,    0, 7, 5,    0, 0, 0],
#   [0, 0, 0,    0, 5, 0,    0, 8, 0],

#   [0, 0, 9,    0, 0, 0,    0, 0, 0],
#   [2, 0, 6,    0, 0, 0,    0, 0, 0],
#   [0, 0, 0,    0, 0, 0,    0, 0, 0]
#]
