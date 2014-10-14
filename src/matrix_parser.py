__author__ = 'tyler'

import re
import math

# Pattern used to identify and remove all spaces.
TRIM_PATTERN = re.compile(r'\s+')
# Match all inner rows.
ROW_PATTERN = re.compile(r'\{.*?\}')
# Match floating point values and allow for fractions... TODO: test me w/ fractions and floating point
EXPR_PATTERN = re.compile(r'[+-]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?(?:/[+-]?[0-9]+\.?[0-9]+(?:[eE][-+]?[0-9]+)?)?')

# Allow math in namespace, no other functions so eval is safe-ish. Would have to extend above regex to support math
# functions though...
EVAL_NS = vars(math).copy()
EVAL_NS['__builtins__'] = None

# Minimum size necessary to represent an empty matrix.
MIN_MATRIX_LEN = 2


def parse_matrix(input):
    # matrix in string form without whitespace
    matrix_str = re.sub(TRIM_PATTERN, '', input)
    matrix = None
    if len(matrix_str) >= MIN_MATRIX_LEN and matrix_str[0] == '{' and matrix_str[len(matrix_str) - 1] == '}':
        # pass in slice removing first/last brace
        matrix = __parse_rows(matrix_str[1:-1])
    return matrix

def __parse_rows(matrix_str):
    matrix = [[]]
    # Split into row strings.
    rows = ROW_PATTERN.findall(matrix_str)
    # Row counter.
    row_num = 0
    # Column counter.
    col_num = 0
    # Look at every row.
    for row in rows:
        # Split row into individual values.
        values = re.findall(EXPR_PATTERN, row)

        if len(matrix) != row_num + 1:
            matrix.append([])
        # Look at each individual value and evaluate it as a number or expression.
        for value in values:
            # Stuff might go bad here if the input is bad.
            matrix[row_num].append(eval(value, EVAL_NS))
            col_num += 1
        # We aren't going to count empty rows for the sake of validity. Stuff will probably go wrong later anyway
        # if we see one of these.
        if len(matrix[row_num]) > 0:
            row_num += 1
    # Don't care if empty matrix, done.
    if len(matrix) > 0:
        row_len = len(matrix[0])
        # Check rows are of appropriate length.
        for row in matrix:
            if len(row) != row_len:
                # Ragged matrix.
    #           matrix = None
                # Done here...
                break
    return matrix



