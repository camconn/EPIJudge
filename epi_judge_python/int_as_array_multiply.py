from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    output = [0]*(len(num1) + len(num2))

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            output[i + j + 1] += num1[i] * num2[j]
            output[i + j] += output[i+j+1] // 10
            output[i + j + 1] %= 10

    # Remove extraneous leading zeros
    while len(output) > 0 and output[0] == 0:
        output.pop(0)

    # If output number is empty, give back a 0
    if len(output) == 0:
        output.append(0)

    output[0] *= sign

    return output


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
