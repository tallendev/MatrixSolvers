#!usr/bin/python

__author__ = 'tyler'

import sys
from src.matrix_parser import parse_matrix

# Exit due to invalid number of arguments.
INVALID_ARG_COUNT = 1
# Exit due to file without proper permissions, or file does not exist.
INVALID_FILE = 2
# Exit due to bad matrix input.
INVALID_INPUT = 3

# Index in args array of program name
PROGRAM_NAME = 0
# Index in args array of method to use in solving the matrix.
SOLVE_METHOD = 1
# Index in args array of optional file name
FILE_NAME = 2

# python [program_name] solve_method
NUM_PROMPT_ARGS = 2
# python [program_name] solve_method [file_input]
NUM_FILE_ARGS = 3


def main():
    num_args = len(sys.argv)
    file = None
    # Prompt user for input
    if num_args == NUM_PROMPT_ARGS:
        print("Input a matrix:\n")
        file = sys.stdin
    # Open specified file
    elif num_args == NUM_FILE_ARGS:
        file = open(sys.argv[FILE_NAME], "r", encoding="utf-8")
    # Usage
    else:
        usage(INVALID_ARG_COUNT, "Invalid number of arguments.")
    input = file.read()
    parse_matrix(input)

def usage(exit_status, message):
    #TODO: finish usage
    print(message + "\nUsage: python " + sys.argv[PROGRAM_NAME] + " solve_method ["
          "file_input]\nValid Solve Methods:\ngaussian: Basic Gaussian Elimination using "
          "Backwards Substitution\ngaussian_pivot: Gaussian Elimination using Partial "
          "Pivots\n\n\nValid Input Format: {{a11, a12, ...}, {a21, a22, ...}, ...}\nAny "
          "whitespace is accepted.")
    sys.exit(exit_status)



main()