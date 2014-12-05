#!usr/bin/python

__author__ = 'tyler'

# Author: Tyler Allen
# Date Created: 10/13/2014
# Last Modified: 10/14/2014
# A program for coordinating the use of the 5 solver methods being implemented for the Math 362 honors project.
# This program accepts a solution method (from the ones provided), and an optional file. If a file is not provided,
# the user will be prompted to input a matrix by hand.
#
# TODO: Finish this doc

import sys
import os
import copy
from src.matrix_parser import parse_matrix
from src.gaussian import Gaussian
from src.gaussian_pivot import GaussianPivot
from src.jacobi import Jacobi
from src.gauss_seidel import GaussSeidel

# Exit due to invalid number of arguments.
INVALID_ARG_COUNT = 1
# Exit due to file without proper permissions, or file does not exist.
INVALID_FILE = 2
# Exit due to bad matrix input.
INVALID_INPUT = 3
# Bad solution method.
INVALID_METHOD = 4

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

# available solve method dictionary
DIRECT_METHODS = {'gaussian' : Gaussian,
                  'gaussian_pivot' : GaussianPivot}

ITERATIVE_METHODS = {'jacobi' : Jacobi,
                     'gauss_seidel' : GaussSeidel}

def main():
    num_args = len(sys.argv)
    file = None
    # Prompt user for input
    if num_args == NUM_PROMPT_ARGS:
        print("Input a matrix:\n")
        file = sys.stdin
    # Open specified file
    elif num_args == NUM_FILE_ARGS:
        if not os.access(sys.argv[FILE_NAME], os.F_OK):
            usage(INVALID_FILE, "File not found: " + sys.argv[FILE_NAME])
        elif not os.access(sys.argv[FILE_NAME], os.R_OK):
            usage(INVALID_FILE, "File could not be read: " + sys.argv[FILE_NAME])
        file = open(sys.argv[FILE_NAME], "r", encoding="utf-8")


    # Usage
    else:
        usage(INVALID_ARG_COUNT, "Invalid number of arguments.")

    if not (sys.argv[SOLVE_METHOD] in DIRECT_METHODS or sys.argv[SOLVE_METHOD] in ITERATIVE_METHODS):
        usage(INVALID_METHOD, "Solve method provided on command line does not exist: " + sys.argv[SOLVE_METHOD])

    input = file.read()
    matrix = parse_matrix(input)
    solution = [[]]
    if matrix is None:
        usage(INVALID_INPUT, "There was an error in the input.")
    else:
        print("Original Matrix:\n" + str(matrix) + "\n")
        if len(matrix) == 0:
            print("The matrix was empty.")
        else:
            if (sys.argv[SOLVE_METHOD] in DIRECT_METHODS):
                solution = DIRECT_METHODS[sys.argv[SOLVE_METHOD]](copy.deepcopy(matrix))
            else:
                solution = ITERATIVE_METHODS[sys.argv[SOLVE_METHOD]](copy.deepcopy(matrix), 25, .0003)
    if solution.has_unique_solution():
        print(solution)
    else:
        print("Matrix has no unique solution.")


def usage(exit_status, message):
    #TODO: finish usage
    print(message + "\nUsage: python " + sys.argv[PROGRAM_NAME] + " solve_method ["
          "file_input]\n\nValid Solve Methods:\ngaussian: Basic Gaussian Elimination using "
          "Backwards Substitution\ngaussian_pivot: Gaussian Elimination using Partial "
          "Pivots\n\nValid Input Format: {{a11, a12, ...}, {a21, a22, ...}, ...}\nAny "
          "whitespace is accepted.")
    sys.exit(exit_status)



main()