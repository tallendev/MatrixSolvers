__author__ = 'tyler'

import re
TRIM_PATTERN = re.compile(r'\s+')
ROW_PATTERN = re.compile(r'{\d+,')

# Minimum size necessary to represent an empty matrix.
MIN_MATRIX_LEN = 2


def parse_matrix(input):
    # matrix in string form without whitespace
    matrix_str = re.sub(TRIM_PATTERN, input)
    matrix = None
    if len(matrix_str) >= MIN_MATRIX_LEN and matrix_str[0] == '{':
        matrix = __parse_rows(matrix_str)
    return matrix

def __parse_rows(matrix_str):


