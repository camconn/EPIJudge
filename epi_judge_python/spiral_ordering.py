from typing import List

from test_framework import generic_test

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    order = []
    if len(square_matrix) == 0:
        return order

    direction = RIGHT

    row, col = 0, 0
    rows = len(square_matrix)
    cols = len(square_matrix[0])

    #u_bound, r_bound, d_bound, l_bound = 0, cols-1, rows-1, 0
    u_bound, r_bound, d_bound, l_bound = -1, cols, rows, -1

    while True:
        if abs(l_bound - r_bound) <= 1 or abs(u_bound - d_bound) <= 1:
            break

        if direction == RIGHT:
            order.append(square_matrix[row][col])
            col += 1

            if col == r_bound:
                # hit the right wall, change direction and bounds
                col = r_bound - 1
                row = u_bound + 2
                direction = DOWN
                r_bound -= 1
                

        elif direction == DOWN:
            order.append(square_matrix[row][col])
            row += 1

            if row >= d_bound:
                # hit the bottom wall, change direction and bounds
                row = d_bound - 1
                col = r_bound - 1
                direction = LEFT
                d_bound -= 1

        elif direction == LEFT:
            order.append(square_matrix[row][col])
            col -= 1

            if col == l_bound:
                # hit the left wall, change direction and bounds
                col = l_bound + 1
                row = d_bound - 1

                direction = UP
                l_bound += 1

        elif direction == UP:
            order.append(square_matrix[row][col])
            row -= 1

            if row == u_bound + 1:
                # hit the left wall, change direction and bounds
                row = u_bound + 2
                col = l_bound + 1
                direction = RIGHT
                u_bound += 1

        else:
            raise Exception("Invalid direction: {}".format(direction))

    return order


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
